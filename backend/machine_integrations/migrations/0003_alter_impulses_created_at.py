# Generated by Django 4.2.4 on 2023-08-24 12:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('machine_integrations', '0002_alter_impulses_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impulses',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
