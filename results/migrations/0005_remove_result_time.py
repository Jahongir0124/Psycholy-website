# Generated by Django 3.2.3 on 2021-11-12 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0004_alter_result_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='time',
        ),
    ]
