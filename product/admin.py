from django.contrib import admin
from .models import Category, Product


class MyModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'modified_at')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category)
admin.site.register(Product, MyModelAdmin)
