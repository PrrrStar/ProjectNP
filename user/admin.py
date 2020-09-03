from django.contrib import admin
from .models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(User, UserAdmin)
