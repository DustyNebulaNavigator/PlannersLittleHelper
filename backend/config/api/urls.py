from rest_framework.routers import DefaultRouter
from machine_integrations.api.urls import impulse_router
from django.urls import path, include

router = DefaultRouter()

router.registry.extend(impulse_router.registry)

urlpatterns = [
    path('', include(router.urls))
]
