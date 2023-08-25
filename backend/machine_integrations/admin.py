from django.contrib import admin

from .models import Impulses


class AdminImpulses(admin.ModelAdmin):
    list_display = ('machine_name', 'product_name', 'sensor_counter', 'sensor_timestamp', 'created_at')

admin.site.register(Impulses, AdminImpulses)