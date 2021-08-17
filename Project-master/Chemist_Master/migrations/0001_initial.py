# Generated by Django 3.0.2 on 2020-03-07 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChemistRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.EmailField(max_length=50, verbose_name='Email')),
                ('chemistpwd', models.CharField(max_length=20, verbose_name='Password')),
                ('chemistfname', models.CharField(default='', max_length=20, verbose_name='First_Name')),
                ('chemistmname', models.CharField(default='', max_length=20, verbose_name='Middle_Name')),
                ('chemistlname', models.CharField(default='', max_length=20, verbose_name='Last_Name')),
                ('chemistaddress', models.CharField(default='', max_length=20, verbose_name='Address')),
                ('chemistcity', models.CharField(default='', max_length=20, verbose_name='City')),
                ('chemistarea', models.CharField(default='', max_length=20, verbose_name='Area')),
                ('chemistpincode', models.IntegerField(default='', verbose_name='Pincode')),
                ('chemistcontactno', models.IntegerField(default='', verbose_name='Contact_No')),
                ('chemistphoto', models.FileField(upload_to='upload', verbose_name='store certificate')),
            ],
        ),
    ]
