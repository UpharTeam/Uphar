# Generated by Django 2.1.5 on 2021-03-30 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0008_auto_20210326_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inc',
            name='opname',
            field=models.CharField(default='', max_length=80),
        ),
    ]