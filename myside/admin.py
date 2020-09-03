from django.contrib import admin
from .models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', )





class CategoryAdmin(admin.ModelAdmin):
    list_display = ('first','second' )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
