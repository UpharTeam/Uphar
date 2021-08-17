from django.contrib import admin
from .models import doctors,patient,adminapp,Doctor_Department

class doctoradmin(admin.ModelAdmin):
    list_display=['doc_fname','doc_email','doc_dep']
    list_filter=['doc_fname','doc_email','doc_mob']

class patientadmin(admin.ModelAdmin):
    list_display=['pat_fname','pat_email']
    list_filter=['pat_fname','pat_email','pat_mob']


admin.site.register(doctors,doctoradmin)
admin.site.register(patient,patientadmin)
admin.site.register(adminapp)
admin.site.register(Doctor_Department)

