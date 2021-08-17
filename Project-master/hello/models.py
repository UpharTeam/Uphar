from django.db import models

# Create your models here.
ic_CHOICES=[("open","open"),("close","close"),]
class cat(models.Model):
    catn=models.CharField(max_length=80)
    dhmail=models.CharField(max_length=80)
class com(models.Model):        
    coname=models.CharField(max_length=80)
    cohmail=models.CharField(max_length=80)
    copmail=models.CharField(max_length=80)
class inc(models.Model):
    incdes=models.TextField(max_length=800,default='')
    buildname=models.CharField(max_length=80,default='')
    wardname=models.CharField(max_length=80,default='')
    roomname=models.CharField(max_length=80,default='')
    bedname=models.CharField(max_length=10,default='')
    catname=models.CharField(max_length=80,default='')
    opname=models.CharField(max_length=80,default='')
    
