from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin

@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug','category','img','description','price','stock','available_display','created_at','modified_at')

    prepopulated_fields = {'slug':('name',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('content',)

@admin.register(Recomment)
class RecommentAdmin(admin.ModelAdmin):
    list_display=('content',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display=('name','img')



#@admin.register(Product_has_brand)
#class Product_has_brandAdmin(admin.ModelAdmin):
#    list_display=()

