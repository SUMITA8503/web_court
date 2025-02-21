# Generated by Django 5.1 on 2024-11-15 19:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myadmin', '0014_rename_client_id_case_client_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hearing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nextdate', models.DateField()),
                ('remarks', models.TextField()),
                ('status', models.CharField(max_length=30)),
                ('description', models.TextField(default='')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.case')),
            ],
            options={
                'db_table': 'hearing',
            },
        ),
    ]
