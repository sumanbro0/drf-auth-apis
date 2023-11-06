from django.contrib import admin
from .models import Image,Product
# Register your models here.


class ProductImageAdmin(admin.StackedInline):
    model = Image

class ProductAdmin(admin.ModelAdmin):
    inlines=[ProductImageAdmin]

admin.site.register(Product, ProductAdmin)