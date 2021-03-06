# Generated by Django 3.1.4 on 2021-01-11 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0006_auto_20210110_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='department',
            field=models.CharField(choices=[('Allergists', 'Allergists'), ('Anesthesiologists', 'Anesthesiologists'), ('Cardiologists', 'Cardiologists'), ('Dermatologists', 'Dermatologists'), ('Endocrinologists', 'Endocrinologists'), ('Gastroenterologists', 'Gastroenterologists'), ('Critical Care Medicine Specialists', 'Critical Care Medicine Specialists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists')], max_length=100),
        ),
    ]
