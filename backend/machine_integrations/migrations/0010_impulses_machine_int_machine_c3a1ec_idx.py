# Generated by Django 4.2.4 on 2023-10-26 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine_integrations', '0009_alter_impulses_machine_name'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='impulses',
            index=models.Index(fields=['machine_name', '-sensor_counter'], name='machine_int_machine_c3a1ec_idx'),
        ),
    ]