# Generated by Django 3.1.7 on 2021-03-16 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin1', '0015_doctor_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_department',
            name='end_time',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='doctor_department',
            name='start_time',
            field=models.CharField(default='', max_length=50),
        ),
    ]