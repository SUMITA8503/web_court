# Generated by Django 5.1.1 on 2024-11-15 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0011_alter_case_fir_copy_alter_client_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='title',
            new_name='case_title',
        ),
    ]
