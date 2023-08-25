from rest_framework import serializers
from ..models import Impulses


class ImpulseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impulses
        fields = ('machine_name', 'product_name', 'sensor_counter', 'sensor_timestamp', 'created_at')


class CycleTimeSerializer(serializers.Serializer):
    machine_name = serializers.CharField(max_length=200)
    cycle_time = serializers.FloatField()
    cycle_time_calc_start = serializers.JSONField()
    cycle_time_calc_end = serializers.JSONField()
