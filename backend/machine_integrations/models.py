from django.db import models


class Impulses(models.Model):
    machine_name = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255, blank=True, default='Missing', null=True)
    sensor_counter = models.IntegerField()
    sensor_timestamp = models.IntegerField()
    created_at = models.DateTimeField()

    def __str__(self):
        return f"{machine_name}"

class Machines(models.Model):
    machine_name = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=255)