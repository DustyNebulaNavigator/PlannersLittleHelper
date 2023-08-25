from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CycleTimeViewSet, ImpulseViewSet

impulse_router = DefaultRouter()
impulse_router.register(r'impulses', ImpulseViewSet)
impulse_router.register(r'cycletimes', CycleTimeViewSet, basename='virtualmodel')