from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
user = get_user_model()

class UserAdmin(admin.ModelAdmin):
    search_fields = ["email"]
    list_display = ['email','user_name','active','staff','superuser']
    list_filter = ("email","active","staff","superuser")
    fieldsets = (
        ('Accounts Detail',{'fields':("email","user_name","password")}),
        ('Status',{'fields':("active",)}),
        ('Personal info', {'fields': ('first_name',"last_name","telephone_No")}),
        ('permissions',{'fields':('superuser','staff')}),
    )

    ordering = ('email',)



admin.site.register(user, UserAdmin)