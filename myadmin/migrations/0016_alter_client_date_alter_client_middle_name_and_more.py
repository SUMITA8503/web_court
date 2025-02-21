# Generated by Django 5.1 on 2024-11-25 10:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0015_client_middle_name_staff_dob_staff_education_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='client',
            name='middle_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='staff',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
