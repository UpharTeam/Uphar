# Generated by Django 3.1.4 on 2021-01-10 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0003_remove_book_a'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='department',
            field=models.CharField(choices=[('Allergists', 'Allergists'), ('Anesthesiologists', 'Anesthesiologists'), ('Cardiologists', 'Cardiologists'), ('Dermatologists', 'Dermatologists'), ('Endocrinologists', 'Endocrinologists'), ('Gastroenterologists', 'Gastroenterologists'), ('Critical Care Medicine Specialists', 'Critical Care Medicine Specialists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists')], default='Allergists', max_length=500),
        ),
    ]
