from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # adminのページで示すフィールド
    list_display = ['id', 'email', 'created_date', 'last_login_date', 'is_staff', 'is_superuser']
    # レコードの検索に使えるフィールド
    search_fields = ['id', 'email']
    # 読み取り専用のフィールド
    readonly_fields=['id', 'created_date', 'last_login_date']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ()
