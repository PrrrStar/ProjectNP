from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'myside/index.html', {'products': products, 'categories': categories})


def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id)
    return render(request, 'myside/detail.html', {'product': product})

def product_in_category(request, category_slug = None):
    current_category = None
    products = Product.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category, available_display=True)

    return render(request, 'myside/list.html', {
                'current_category': current_category,
                'products': products,
                })
