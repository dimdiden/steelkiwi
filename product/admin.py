from django.contrib import admin
from .models import Category, Product


class CategoryModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ProductModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'modified_at')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Product, ProductModelAdmin)
