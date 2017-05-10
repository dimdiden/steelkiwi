from django.contrib import admin
from .models import Category, Product


class MyModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'modified_at')


admin.site.register(Category)
admin.site.register(Product, MyModelAdmin)
