# Generated by Django 3.1.4 on 2021-01-09 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin1', '0011_doctors_doc_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='doc_dob',
            field=models.CharField(default='', max_length=15),
        ),
    ]
