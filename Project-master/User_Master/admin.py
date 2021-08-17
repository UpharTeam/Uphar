from django.contrib import admin

# Register your models here.

from .models import UserRegister,cart,UserQuery

class UserRegisterAdmin(admin.ModelAdmin):
        list_display=['uid','userfname','usermname','userlname','useraddress','usercity','userarea','userpincode','usercontactno']


admin.site.register(UserRegister,UserRegisterAdmin)
admin.site.register(cart)
admin.site.register(UserQuery)