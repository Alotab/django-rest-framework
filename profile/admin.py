from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'profile_picture')
    search_fields = ('username', 'first_name', 'last_name', 'email')

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('profile_picture',)}),
    )
admin.site.register(User, UserAdmin)
