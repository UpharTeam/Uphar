# Generated by Django 3.1.7 on 2021-03-16 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin1', '0017_auto_20210316_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_department',
            name='doc_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='admin1.doctors'),
        ),
    ]
