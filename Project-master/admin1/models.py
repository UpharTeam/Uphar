from django.db import models

# For Doctor Details

class doctors(models.Model):
    doc_fname=models.CharField(max_length=50)
    doc_mname=models.CharField(max_length=50)
    doc_lname=models.CharField(max_length=50)
    doc_email=models.EmailField(max_length=100,unique=True)
    doc_dob=models.CharField(max_length=15,default='')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    doc_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    doc_address=models.TextField(max_length=200)
    doc_city=models.CharField(max_length=50)
    doc_pcode=models.IntegerField(default='')    
    doc_mob=models.IntegerField(default='')
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
    doc_dep = models.CharField(max_length=1000, choices=DEPARTMENT_CHOICES, default='')
    doc_country=models.CharField(max_length=50,default='')
    doc_state=models.CharField(max_length=50,default='')
    

    def __str__(self):
        return self.doc_fname +" "+self.doc_lname

    #For Patient Details

class patient(models.Model):
    pat_fname=models.CharField(max_length=50)
    pat_mname=models.CharField(max_length=50)
    pat_lname=models.CharField(max_length=50)
    pat_email=models.EmailField(max_length=100,unique=True)
    pat_dob=models.CharField(max_length=15,default='')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    pat_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    pat_address=models.TextField(max_length=200)
    pat_city=models.CharField(max_length=50)
    pat_pcode=models.IntegerField(default='')    
    pat_mob=models.IntegerField(default='')
    
    

    def __str__(self):
        return self.pat_fname +" "+self.pat_lname

#For Admin Registration (Details) 

class adminapp(models.Model):
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=50,unique=True)
    password=models.CharField(max_length=10)
    mobile=models.IntegerField(default='')
    forgot_pass = models.CharField('Write your password hint',max_length=100,default='')


    def __str__(self):
        return self.username

# Doctor Department...

class Doctor_Department(models.Model):
    doc_name = models.CharField(default='',max_length=100)
    doc_dept = models.CharField(default='',max_length=100)
    DAYS_CHOICES = (
        ('Monday', 'Moday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Tuesday'),
        ('Sunday', 'Sunday'),
    )
    available_day = models.CharField(max_length=100,choices=DAYS_CHOICES)
    available_time = models.CharField(default='',max_length=50)
    end_time = models.CharField(default='',max_length=100)
    

    def __str__(self):
        return self.doc_name
    
# Used for prediction

# class prediction(models.Model):
#     pred_pat_info=models.ForeignKey(patient,on_delete=models.CASCADE,default='')
#     pred_year=models.IntegerField(default='')
#     pred_bed=models.IntegerField(default='')
#     pred_Total_Med=models.IntegerField(default='')