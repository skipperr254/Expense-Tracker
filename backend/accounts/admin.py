from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models

# Register your models here.

User = get_user_model()

class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'user_name', 'first_name')
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
    ordering = ('-start_date', )
    list_display = ('id', 'email', 'user_name', 'first_name', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name', )}),
        ('Permissions', {'fields': ('is_staff', 'is_active', )}),
        ('Personal', {'fields': ('about', )}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})}
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'is_active', 'is_staff')
        })
    )

admin.site.register(User, UserAdminConfig)