# Generated by Django 5.1.1 on 2024-11-19 18:16

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0014_rename_client_id_case_client_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='middle_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='staff',
            name='dob',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='staff',
            name='education',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='date',
            field=models.DateField(default=datetime.date(2024, 11, 19)),
        ),
        migrations.AlterField(
            model_name='staff',
            name='date',
            field=models.DateField(default=datetime.date(2024, 11, 19)),
        ),
    ]
