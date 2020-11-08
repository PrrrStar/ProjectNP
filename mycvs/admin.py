from django.contrib import admin
from .models import *

@admin.register(CVS)
class CVSAdmin(admin.ModelAdmin):
    list_display=['name','latitude','longitude','brand','brand_logo','slug']
    filter_horizontal = ('user',)
    prepopulated_fields = {'slug':('name',)}

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['stock','product','cvs']