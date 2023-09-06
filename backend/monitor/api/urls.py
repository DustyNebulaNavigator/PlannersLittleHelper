from rest_framework.routers import DefaultRouter
from .views import PartNumberViewSet, MonitorCycleTimesViewSet

monitor_router = DefaultRouter()
#monitor_router.register(r'partNr/(?P<part_id>\w+)', PartNumberViewSet, basename='partNrVirtualmodel')
monitor_router.register(r'partNr/(?P<part_id>\d+)', PartNumberViewSet, basename='partNrVirtualmodel')
monitor_router.register(r'partNr/monitor_cycle_times', MonitorCycleTimesViewSet, basename='monitorCycleTimesVirtualmodel')