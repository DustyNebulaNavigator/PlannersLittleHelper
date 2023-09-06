from rest_framework import serializers

class PartNumberSerializer(serializers.Serializer):
    part_nr = serializers.CharField(max_length=200)
    part_description = serializers.CharField(max_length=200)

class MonitorCycleTimesSerializer(serializers.Serializer):
    machine_nr = serializers.CharField(max_length=200)
    part_number = serializers.CharField(max_length=200)
    part_description = serializers.CharField(max_length=200)
    unit_time = serializers.FloatField()