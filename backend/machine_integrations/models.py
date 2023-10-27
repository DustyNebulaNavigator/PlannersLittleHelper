from django.db import models


class Impulses(models.Model):
    machine_name = models.CharField(max_length=255, db_index=True)
    product_name = models.CharField(max_length=255, blank=True, default='Missing', null=True)
    sensor_counter = models.IntegerField(db_index=True)
    sensor_timestamp = models.IntegerField()
    created_at = models.DateTimeField(db_index=True)

    class Meta:
        indexes = [
            models.Index(fields=['machine_name', '-sensor_counter']),
        ]

    def __str__(self):
        #return f"{machine_name}"
        return ""

class Machines(models.Model):
    machine_name = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=255)