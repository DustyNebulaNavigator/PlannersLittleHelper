from django.db.models import Min, Max
from django.utils import timezone
from rest_framework.viewsets import ModelViewSet
from dataclasses import dataclass
from datetime import timedelta, datetime

from ..models import Impulses, Machines
from .serializers import ImpulseSerializer, CycleTimeSerializer, MachineStatusSerializer, AverageCycleTimeSerializer


class ImpulseViewSet(ModelViewSet):
    # Just for testing to see 15 latest datarows.
    queryset = Impulses.objects.order_by('-created_at')[:15]
    serializer_class = ImpulseSerializer

@dataclass
class VirtualModel:
    machine_name: str
    cycle_time: float
    cycle_time_calc_start: int
    cycle_time_calc_end: int

class CycleTimeViewSet(ModelViewSet):
    
    serializer_class = CycleTimeSerializer

    def get_queryset(self):
        
        lis_of_machine_names = [
            'M0153', 'M0083', 'M0082', 'M0081', 'M0151',
            'M0041', 'M0301', 'M0122', 'M0052', 'M0451',
            'M0084', 'M0044', 'M0054', 'M0422', 'M0055',
            'M0253', 'M0056', 'M1003', 'M0281', 'M0091',
            'M0273', 'M0102', 'M0501', 'M0057', 'M0202',
            'M1002', 'M0221', 'M0352', 'M0402', 'M0901',
            'M0051', 'M0025', 'M0123', 'M0042', 'M0101',
            'M0201', 'M0121', 'M0222', 'M0131'
        ]
        """
        lis_of_machine_names = [
            'M0091', 'M0131', 'M0153', 'M0201', 'M0202',
            'M0221', 'M0222', 'M0253', 'M0273', 'M0281',
            'M0301', 'M0352', 'M0402', 'M0422', 'M0451',  
            'M0501', 'M0901', 'M1002', 'M1003'
            
             
        ]
        """
        data = []
        one_day_ago = timezone.now() - timedelta(days=1)
        for machine in lis_of_machine_names:
            
            
            try:

                latest_impulses = Impulses.objects.filter(
                    machine_name=machine,
                    created_at__gte=one_day_ago).order_by('-sensor_counter')[:10].aggregate(
                    Max('sensor_counter'),
                    Min('sensor_counter'),
                    Min('sensor_timestamp'),
                    Max('sensor_timestamp'),
                    Min('created_at'),
                    Max('created_at')
                    )

                cycle_time = (latest_impulses['sensor_timestamp__max'] - latest_impulses['sensor_timestamp__min']) / (latest_impulses['sensor_counter__max']-latest_impulses['sensor_counter__min'])
                cycle_time = round(cycle_time, 2)
                
                cycle_time_calc_start = latest_impulses['created_at__min']
                cycle_time_calc_start = timezone.localtime(cycle_time_calc_start).strftime('%H:%M %d.%m.%Y')

                cycle_time_calc_end = latest_impulses['created_at__max']
                cycle_time_calc_end = timezone.localtime(cycle_time_calc_end).strftime('%H:%M %d.%m.%Y')
            except:
                cycle_time_calc_start = 0
                cycle_time_calc_end = 0
                cycle_time = 0

            data.append(VirtualModel(machine_name=machine, cycle_time=cycle_time, cycle_time_calc_start=cycle_time_calc_start, cycle_time_calc_end=cycle_time_calc_end))
        return data

class MachineStatusViewSet(ModelViewSet):
    queryset = Machines.objects.all()
    serializer_class = MachineStatusSerializer

@dataclass
class AverageCycleTimeVirtualModel:
    avg_interval_cycle_time: float
    #newest_interval_timestamp: int
    newest_interval_timestamp: datetime


class MachineCycleTimeStatsViewSet(ModelViewSet):
    """
    This is used to get data for specific machine in given days.
    """
    serializer_class = AverageCycleTimeSerializer
   
    def get_queryset(self):
        """
        /api/macinecyclestats/?machine_name=M0222&lookback_days=1
        machine_name - injection machine name
        lookback_days - in days
        """
            
        # Get query parameters
        def get_query_parameters():
            machine_name = self.request.query_params.get('machine_name', None)
            try:
                lookback_days = int(self.request.query_params.get('lookback_days', None))
            except:
                lookback_days = 1
            try:
                interval_minutes = int(self.request.query_params.get('interval_minutes', None))
            except:    
                interval_minutes = 15
            
            if not machine_name:
                machine_name = "Missing"
            if lookback_days < 1:
                lookback_days = 1
            if interval_minutes < 1:
                interval_minutes = 1
            return machine_name, lookback_days, interval_minutes
            
        machine_name, lookback_days, interval_minutes = get_query_parameters()

        # Data will be queryed for periode between start_time & end_time
        end_time = timezone.now()
        start_time = end_time - timedelta(days=lookback_days)
        queryset = Impulses.objects.only('sensor_counter', 'sensor_timestamp', 'created_at').filter(
            machine_name=machine_name,
            created_at__range=(start_time, end_time)
            ).order_by('sensor_counter')

        data = []
        interval_start_time = start_time
        while True:
            # Loob will be breaked once interval start time is greater than "end_time = timezone.now()"" was.

            interval_end_time = interval_start_time + timedelta(minutes=interval_minutes) 

            aggregated  = queryset.filter(created_at__range=(interval_start_time, interval_end_time)).aggregate(
                first_cycle_sensor_counter=Min('sensor_counter'),
                last_cycle_sensor_counter=Max('sensor_counter'),
                first_cycle_sensor_timestamp=Min('sensor_timestamp'),
                last_cycle_sensor_timestamp=Max('sensor_timestamp'),
                newest_created_at=Max('created_at')
                )

            try:
                cycle_count_in_selection = aggregated["last_cycle_sensor_counter"] -  aggregated["first_cycle_sensor_counter"]
                total_time_in_selection = aggregated["last_cycle_sensor_timestamp"] -  aggregated["first_cycle_sensor_timestamp"]
                avg_cycle_time = total_time_in_selection / cycle_count_in_selection
                data.append( AverageCycleTimeVirtualModel(avg_interval_cycle_time=avg_cycle_time, newest_interval_timestamp=aggregated["newest_created_at"]))
            except:
                data.append( AverageCycleTimeVirtualModel(avg_interval_cycle_time=0, newest_interval_timestamp=interval_end_time))

            

            interval_start_time = interval_end_time
            if interval_start_time >= end_time:
                break
  
        return data
