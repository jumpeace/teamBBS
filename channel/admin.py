from django.contrib import admin

from .models import Channel

@admin.register(Channel)
class ChannnelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'team', 'created_at', 'updated_at']
    search_fields = ['name', 'team__name']
    readonly_fields= ['id', 'created_at', 'updated_at']
    filter_horizontal = []
    list_filter = []
    fieldsets = []
    ordering = []