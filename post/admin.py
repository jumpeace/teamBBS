from django.contrib import admin

from .models import Channel, Post



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'channel', 'user', 'content', 'created_at', 'updated_at']
    search_fields = ['content', 'user__email', 'channel__name']
    readonly_fields= ['id', 'created_at', 'updated_at']
    filter_horizontal = []
    list_filter = []
    fieldsets = []
    ordering = []

