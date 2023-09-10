from django.contrib import admin
from .models import Category, Expense

# Register your models here.
admin.site.register(Expense)

class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        plural = "Categories"

admin.site.register(Category, CategoryAdmin)