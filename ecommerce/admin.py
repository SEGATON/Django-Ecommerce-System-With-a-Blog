from django.contrib import admin

# Register your models here.
from .models import Product, Category, Brand






class ProductAdmin(admin.ModelAdmin):
	list_display = ('title',)
	prepopulated_fields = {'slug':('title',)}



admin.site.register(Product,ProductAdmin)
admin.site.register(Category)


class BrandAdmin(admin.ModelAdmin):
	list_display = ('name',)
	prepopulated_fields = {'slug':('name',)}

admin.site.register(Brand,BrandAdmin)