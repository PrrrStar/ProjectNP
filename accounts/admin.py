from django.contrib import admin

# Register your models here.

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'username',
        'nickname',
        'gender',
        'birth',
        'profile',
        'is_staff',
        'is_active',
        'date_joined',
        )



   # prepopulated_fields = 
   # filter_horizontal = 