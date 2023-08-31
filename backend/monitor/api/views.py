from rest_framework.viewsets import ModelViewSet
from dataclasses import dataclass

from .serializers import PartNumberSerializer
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
