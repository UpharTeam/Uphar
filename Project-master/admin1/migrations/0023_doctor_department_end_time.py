# Generated by Django 3.1.7 on 2021-03-16 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin1', '0022_auto_20210316_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_department',
            name='end_time',
            field=models.CharField(default='', max_length=100),
        ),
    ]
