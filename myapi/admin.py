from django.contrib import admin
from myapi.models import Profile
from django.contrib.auth.models import User
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display=['id','user','gender','profile_pic','permanent_address']
    search_fields = ['user__first_name']
    list_filter = ['gender','permanent_address__city_name']

admin.site.register(Profile, ProfileAdmin)