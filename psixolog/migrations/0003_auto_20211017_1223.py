# Generated by Django 3.2.3 on 2021-10-17 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psixolog', '0002_register'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='register',
            options={'verbose_name': 'Qatnashuvchi', 'verbose_name_plural': 'Qatnashuvchilar'},
        ),
        migrations.RemoveField(
            model_name='psychologist',
            name='email',
        ),
    ]
