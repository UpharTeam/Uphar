# Generated by Django 3.1.7 on 2021-03-26 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_auto_20210326_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inc',
            name='incdes',
            field=models.TextField(default='', max_length=800),
        ),
    ]
