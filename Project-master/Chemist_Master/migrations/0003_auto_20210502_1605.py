# Generated by Django 3.1.6 on 2021-05-02 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chemist_Master', '0002_chemistregister_forgot_pass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chemistregister',
            name='chemistaddress',
            field=models.CharField(default='', max_length=200, verbose_name='Address'),
        ),
    ]