from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request, 'myside/index.html', {'products': products})
