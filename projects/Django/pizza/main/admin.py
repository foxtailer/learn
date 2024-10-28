from django.contrib import admin
from django.utils.html import mark_safe
from .models import Categories, Ingredient, Product

# Register the Categories model
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}  # Automatically fill the slug based on the name
    search_fields = ('name',)  # Enable search by name

# Register the Ingredient model
@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)  # Enable search by name

# Register the Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'image_preview')
    search_fields = ('name', 'description')
    list_filter = ('category', 'ingredients')  # Filters for category and ingredients
    autocomplete_fields = ('category', 'ingredients')  # Autocomplete for large ingredient/category lists
    prepopulated_fields = {'slug': ('name',)}  # Automatically fill the slug based on the name
    readonly_fields = ('image_preview',)  # Read-only image preview

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return ''
    image_preview.short_description = 'Image Preview'
