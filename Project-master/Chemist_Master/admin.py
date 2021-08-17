from django.contrib import admin
from Chemist_Master.models import ChemistRegister

class ChemistRegisterAdmin(admin.ModelAdmin):
    list_display=['cid','chemistfname','chemistmname','chemistlname','chemistaddress','chemistcity','chemistarea','chemistpincode','chemistcontactno','chemistphoto']

admin.site.register(ChemistRegister,ChemistRegisterAdmin)
