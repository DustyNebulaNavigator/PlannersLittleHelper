# Generated by Django 4.2.4 on 2023-10-26 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine_integrations', '0008_alter_impulses_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impulses',
            name='machine_name',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]
