from django.contrib import admin

from .models import Role

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'team', 'created_at', 'updated_at']
    search_fields = ['name', 'team__name']
    readonly_fields= ['id', 'created_at', 'updated_at']
    filter_horizontal = []
    list_filter = []
    fieldsets = []
    ordering = []
