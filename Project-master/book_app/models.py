from django.db import models


# Create your models here.

class book(models.Model):
    name = models.CharField(max_length=500)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100,unique=True)
    schedule = models.DateTimeField()
    DEPARTMENT_CHOICES = [
    ('Allergists', 'Allergists'), 
    ('Anesthesiologists', 'Anesthesiologists'), 
    ('Cardiologists', 'Cardiologists'), 
    ('Dermatologists', 'Dermatologists'), 
    ('Endocrinologists', 'Endocrinologists'), 
    ('Gastroenterologists', 'Gastroenterologists'), 
    ('Critical Care Medicine Specialists', 'Critical Care Medicine Specialists'), 
    ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), 
    ]
    department = models.CharField(max_length=1000, choices=DEPARTMENT_CHOICES)

    def __str__(self):
        return self.name