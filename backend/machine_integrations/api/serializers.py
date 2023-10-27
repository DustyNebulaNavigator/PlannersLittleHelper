from rest_framework import serializers
from ..models import Impulses, Machines


class ImpulseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impulses
        fields = ('machine_name', 'product_name', 'sensor_counter', 'sensor_timestamp', 'created_at')


class CycleTimeSerializer(serializers.Serializer):
    machine_name = serializers.CharField(max_length=200)
    cycle_time = serializers.FloatField()
    cycle_time_calc_start = serializers.JSONField()
    cycle_time_calc_end = serializers.JSONField()
    

class MachineStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machines
        fields = ('machine_name', 'status')


class AverageCycleTimeSerializer(serializers.Serializer):
    avg_interval_cycle_time = serializers.FloatField()
    #newest_interval_timestamp = serializers.JSONField()
    newest_interval_timestamp = serializers.DateTimeField()
