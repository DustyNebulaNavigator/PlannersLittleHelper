from rest_framework.routers import DefaultRouter
from django.urls import path, include

from machine_integrations.api.urls import impulse_router
from monitor.api.urls import monitor_router

router = DefaultRouter()

router.registry.extend(impulse_router.registry)
router.registry.extend(monitor_router.registry)

urlpatterns = [
    path('', include(router.urls))
]
