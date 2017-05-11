from django.contrib import admin
from .models import Category, Product

"""
Prepopulate slug fields by name.
Display created_at modified_at field in admin page for Product model
"""


class CategoryModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ProductModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'modified_at')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Product, ProductModelAdmin)
