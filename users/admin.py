from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['staff', 'department', 'phone']
    list_display_links = ['staff']
    list_per_page = 10

admin.site.register(Profile, ProfileAdmin)
