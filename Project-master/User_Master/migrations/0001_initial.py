# Generated by Django 3.0.2 on 2020-03-07 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.EmailField(max_length=50, unique='True', verbose_name='Email')),
                ('userpwd', models.CharField(max_length=20, verbose_name='Password')),
                ('userfname', models.CharField(default='', max_length=20, verbose_name='First_Name')),
                ('usermname', models.CharField(default='', max_length=20, verbose_name='Middle_Name')),
                ('userlname', models.CharField(default='', max_length=20, verbose_name='Last_Name')),
                ('useraddress', models.CharField(default='', max_length=20, verbose_name='Address')),
                ('usercity', models.CharField(default='', max_length=30, verbose_name='City')),
                ('userarea', models.CharField(default='', max_length=20, verbose_name='Area')),
                ('userpincode', models.IntegerField(default='', verbose_name='Pincode')),
                ('usercontactno', models.IntegerField(default='', verbose_name='Contact_No')),
            ],
        ),
    ]