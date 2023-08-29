from django.db.models import Min, Max
from django.utils import timezone
from rest_framework.viewsets import ModelViewSet
from dataclasses import dataclass

from ..models import Impulses, Machines
from .serializers import ImpulseSerializer, CycleTimeSerializer, MachineStatusSerializer


class ImpulseViewSet(ModelViewSet):
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
        """
        lis_of_machine_names = [
            'M0153', 'M0083', 'M0082', 'M0081', 'M0151',
            'M0041', 'M0301', 'M0122', 'M0052', 'M0451',
            'M0084', 'M0044', 'M0054', 'M0422', 'M0055',
            'M0253', 'M0056', 'M1003', 'M0281', 'M0091',
            'M0273', 'M0102', 'M0501', 'M0057', 'M0202',
            'M1002', 'M0221', 'M0352', 'M0402', 'M0901',
            'M0051', 'M0025', 'M0123', 'M0042', 'M0101',
            'M0201', 'M0121', 'M0222', 'M0131', 'OTSI'
        ]
        """
        lis_of_machine_names = [
            'M0091', 'M0131', 'M0153', 'M0201', 'M0202',
            'M0221', 'M0222', 'M0253', 'M0273', 'M0281',
            'M0301', 'M0352', 'M0402', 'M0422', 'M0451',  
            'M0501', 'M0901', 'M1002', 'M1003'
            
             
        ]
        data = []
        for machine in lis_of_machine_names:
            try:
                latest_impulses = Impulses.objects.order_by('-sensor_counter').filter(machine_name=machine)[:10].aggregate(
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
                oldest_record = 0



            data.append(VirtualModel(machine_name=machine, cycle_time=cycle_time, cycle_time_calc_start=cycle_time_calc_start, cycle_time_calc_end=cycle_time_calc_end))


        return data

class MachineStatusViewSet(ModelViewSet):
    queryset = Machines.objects.all()
    serializer_class = MachineStatusSerializer
    