from django.urls import path, include

app_name = 'myside'

urlpatterns = [
    path('', main, name='product_all'),
]
