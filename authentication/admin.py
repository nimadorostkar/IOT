from django.contrib import admin
from . import models
from django.contrib.admin.models import LogEntry
from .models import Profile



admin.site.site_header= " حساب کاربری "
admin.site.site_title= " حساب های کاربری "
admin.site.register(LogEntry)





#------------------------------------------------------------------------------
class ProfileAdmin(ImportExportModelAdmin):
    list_display = ('user_name','phone','address')
    search_fields = ['user_name', 'phone', 'address']

admin.site.register(models.Profile, ProfileAdmin)
