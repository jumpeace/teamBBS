from django.contrib import admin

from .models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at']
    search_fields = ['name']
    readonly_fields= ['id', 'created_at', 'updated_at']
    filter_horizontal = []
    list_filter = []
    fieldsets = []
    ordering = []
