# Generated by Django 2.1.5 on 2021-04-23 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0010_auto_20210413_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inc',
            name='opname',
            field=models.CharField(default='', max_length=80),
        ),
    ]
