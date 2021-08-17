# Generated by Django 3.1.7 on 2021-03-15 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin1', '0014_adminapp_forgot_pass'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_day', models.CharField(choices=[('Monday', 'Moday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Tuesday'), ('Sunday', 'Sunday')], max_length=100)),
                ('start_time', models.TimeField(default='')),
                ('end_time', models.TimeField(default='')),
                ('doc_name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='admin1.doctors')),
            ],
        ),
    ]
