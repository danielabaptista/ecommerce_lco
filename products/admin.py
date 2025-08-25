from django.contrib import admin
from .models import Product, Category, Location

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "stock", "created_at")
    list_filter = ("category","locations",)
    search_fields = ("name", "description")
    filter_horizontal = ("locations",) 

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "address")