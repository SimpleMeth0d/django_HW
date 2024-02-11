from django.contrib import admin

# Register your models here.

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)
    list_filter = ('title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'purchase_price', 'category',)
    list_filter = ('category',)
    search_fields = ('title', 'description',)