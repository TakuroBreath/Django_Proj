from django.contrib import admin

from catalog.models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'category', 'name', 'price',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)