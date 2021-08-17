from django.db import models


# Chemist Details
class ChemistRegister(models.Model):
    cid=models.EmailField(max_length=50,verbose_name='Email')
    chemistpwd=models.CharField(max_length=20,verbose_name='Password')
    chemistfname=models.CharField(max_length=20,default='',verbose_name='First_Name')
    chemistmname=models.CharField(max_length=20,default='',verbose_name='Middle_Name')
    chemistlname=models.CharField(max_length=20,default='',verbose_name='Last_Name')
    chemistaddress=models.CharField(max_length=200,default='',verbose_name='Address')
    chemistcity=models.CharField(max_length=20,default='',verbose_name='City')
    chemistarea=models.CharField(max_length=20,default='',verbose_name='Area')
    chemistpincode=models.IntegerField(default='',verbose_name='Pincode')
    chemistcontactno=models.IntegerField(default='',verbose_name='Contact_No')
    chemistphoto = models.FileField(upload_to   = 'upload',verbose_name='store certificate')
    forgot_pass = models.CharField('Write your password hint',max_length=100,default='')
    def __str__(self):
        return self.cid

