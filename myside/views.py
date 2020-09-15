from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Q

from .models import *
from .forms import *


# Create your views here.
def get_product_queryset(query=None):
    queryset = []
    queries = query.split(' ') #백종원 도시락 => ['백종원', '도시락']
    for q in queries:
        products = Product.objects.filter(
            Q(name__icontains=q)|
            Q(description__icontains=q)
        ).distinct()

        for product in products:
            queryset.append(product)
    return list(set(queryset))


def index(request):
    query = ""
    if request.GET:
        query = request.GET['q']
        products = get_product_queryset(query)
    else:
        products = Product.objects.all()

    categories = Category.objects.all()
    return render(request, 'myside/index.html', {'products': products, 'categories': categories, 'query':query})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    categories = Category.objects.all()

    return render(request, 'myside/detail.html', {'product': product, 'categories': categories})

def comment_create(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(product=product, content=content)
            comment.save()
            return HttpResponseRedirect(product.get_absolute_url())
    else:
        comment_from = CommentForm()
    
    context = {
        'comment_form':comment_from,
        }
    return render(request, 'myside/detail.html', context)
    
def reply_create(request, product_id, id):
    product = get_object_or_404(Product, id=product_id)
    comment = get_object_or_404(Comment, id=id)
    if request.method == 'POST':
        reply_form = ReplyForm(request.POST or None)
        if reply_form.is_valid():
            content = request.POST.get('content')
            reply = Reply.objects.create(comment=comment, content=content)
            reply.save()
            return HttpResponseRedirect(product.get_absolute_url())
    else:
        reply_from = ReplyForm()
    
    context = {
        'reply_form':comment_from,
        }
    return render(request, 'myside/detail.html', context)
    


def product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(
            category=current_category, available_display=True)

    return render(request, 'myside/list.html', {
        'current_category': current_category,
        'products': products,
        'categories' : categories,
    })



from .models import *
from .serializers import ProductCategorySerializer
from .serializers import ProductSerializer
from .serializers import CommentSerializer
from .serializers import ReplySerializer

from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'product-categories':reverse(ProductCategoryList.name, request=request),
            'products':reverse(ProductList.name, request=request),
        })

class ProductCategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = ProductCategorySerializer
    name = 'productcategory-list'

class ProductCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = ProductCategorySerializer
    name = 'productcategory-detail'


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    name='product-list'

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    name='product-detail'

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name='comment-list'

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name='comment-detail'

class ReplyList(generics.ListCreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    name='reply-list'

class ReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    name='reply-detail'