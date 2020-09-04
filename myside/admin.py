from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('content',)

@admin.register(Recomment)
class RecommentAdmin(admin.ModelAdmin):
    list_display=('content',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display=('name','img')


admin.site.register(Category, MPTTModelAdmin)

#@admin.register(Product_has_brand)
#class Product_has_brandAdmin(admin.ModelAdmin):
#    list_display=()

