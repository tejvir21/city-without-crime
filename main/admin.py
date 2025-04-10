from django.contrib import admin
from .models import PoliceStation, Complaint, Criminal, Emergency

# Register your models here.

# Customize Police Station Admin
class PoliceStationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'head_officer', 'phone', 'mobile')
    search_fields = ('name', 'head_officer')
    list_filter = ('address',)


# Customize Complaint Admin
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'description', 'police_station', 'status', 'created_at')
    search_fields = ('description', 'user__username', 'police_station__name')
    list_filter = ('status', 'created_at')
    ordering = ('-created_at',)


# Customize Criminal Admin
class CriminalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'height', 'weight', 'crime_level', 'status')
    search_fields = ('name', 'crime_level', 'status')
    list_filter = ('gender', 'crime_level', 'status')


# Customize Emergency Admin
class EmergencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'created_at')
    search_fields = ('description',)
    ordering = ('-created_at',)


# Register Models with Admin
admin.site.register(PoliceStation, PoliceStationAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Criminal, CriminalAdmin)
admin.site.register(Emergency, EmergencyAdmin)
