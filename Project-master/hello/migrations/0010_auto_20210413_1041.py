# Generated by Django 3.1.7 on 2021-04-13 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0009_auto_20210330_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inc',
            name='opname',
            field=models.EmailField(default='', max_length=80),
        ),
    ]