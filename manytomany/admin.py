from django.contrib import admin

from .models import (
    User_Team, 
    User_Role,
)


@admin.register(User_Team)
class UserTeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'team', 'is_owner', 'created_at', 'updated_at']
    search_fields = ['user__email', 'team__name']
    readonly_fields= ['id', 'created_at', 'updated_at']
    filter_horizontal = []
    list_filter = []
    fieldsets = []
    ordering = []

@admin.register(User_Role)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'role', 'created_at', 'updated_at']
    search_fields = ['user__email', 'role__name']
    readonly_fields= ['id', 'created_at', 'updated_at']
    filter_horizontal = []
    list_filter = []
    fieldsets = []
    ordering = []
