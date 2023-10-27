from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CycleTimeViewSet, ImpulseViewSet, MachineStatusViewSet, MachineCycleTimeStatsViewSet

impulse_router = DefaultRouter()
impulse_router.register(r'impulses', ImpulseViewSet)
impulse_router.register(r'cycletimes', CycleTimeViewSet, basename='cycletimesVirtualmodel')
impulse_router.register(r'statuses', MachineStatusViewSet)
impulse_router.register(r'macinecyclestats', MachineCycleTimeStatsViewSet, basename='macinecyclestats')
