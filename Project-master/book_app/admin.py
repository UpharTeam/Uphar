from django.contrib import admin
from .models import book
# Register your models here.

class newadmintable(admin.ModelAdmin):
    list_display=['name','email']
    list_filter=['name','email']
admin.site.register(book,newadmintable)