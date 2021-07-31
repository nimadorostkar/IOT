from django.contrib import admin
from . import models
from django.contrib.admin.models import LogEntry
from .models import Profile





#------------------------------------------------------------------------------
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_name','phone','address')
    search_fields = ['user_name', 'phone', 'address']

admin.site.register(models.Profile, ProfileAdmin)
