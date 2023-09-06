from rest_framework.viewsets import ModelViewSet
from dataclasses import dataclass

from .serializers import PartNumberSerializer, MonitorCycleTimesSerializer
from ..utils.monitor import Monitor

@dataclass
class VirtualModel:
    part_nr: str
    part_description: str

class PartNumberViewSet(ModelViewSet):
    serializer_class = PartNumberSerializer

    def get_queryset(self):
        part_id = self.kwargs.get('part_id')

        monitor = Monitor()
        data = monitor.get_part_name_based_on_id(part_id)[0]

        return [VirtualModel(part_nr=data.get('PartNumber'), part_description=data.get('Description'))]

class MonitorCycleTimesViewSet(ModelViewSet):
    serializer_class = MonitorCycleTimesSerializer
    def get_queryset(self):
        monitor = Monitor()
        # Get all currently not finished 
        running_work_intervals = monitor.get_running_work_intervals()
        work_order_operation_ids = [work_interval.get('OperationId') for work_interval in running_work_intervals if work_interval.get('OperationId') != None]
        manuf_order_operations = monitor.get_manufacturing_order_operations(work_order_operation_ids)
        work_centers = monitor.get_all_work_centers()

        # Add work center number
        for manuf_operation in manuf_order_operations:
            manuf_operation['machine_nr'] = [center.get('Number') for center in work_centers if center.get('Id') == manuf_operation.get('WorkCenterId')][0]
            
        workcenters_cycle_time = []
        for manuf_order_operation in manuf_order_operations:
            part_number = manuf_order_operation.get('Part').get('PartNumber')
            part_description = manuf_order_operation.get('Part').get('Description')
            try:
                unit_time = float(manuf_order_operation.get('OperationRow').get('UnitTime'))/10000000
            except AttributeError:
                unit_time = 0
            machine_nr = manuf_order_operation.get('machine_nr')
            workcenter_cycle_time = {
                'part_number': part_number,
                'part_description': part_description,
                'unit_time': unit_time,
                'machine_nr': machine_nr,
            }
            workcenters_cycle_time.append(workcenter_cycle_time)

        return workcenters_cycle_time