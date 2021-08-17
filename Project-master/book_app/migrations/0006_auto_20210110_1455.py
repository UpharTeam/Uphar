# Generated by Django 3.1.5 on 2021-01-10 14:55

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0005_auto_20210110_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='department',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Allergists', 'Allergists'), ('Anesthesiologists', 'Anesthesiologists'), ('Cardiologists', 'Cardiologists'), ('Dermatologists', 'Dermatologists'), ('Endocrinologists', 'Endocrinologists'), ('Gastroenterologists', 'Gastroenterologists'), ('Critical Care Medicine Specialists', 'Critical Care Medicine Specialists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists')], default='', max_length=500),
        ),
    ]
