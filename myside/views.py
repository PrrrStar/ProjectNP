from .serializers import ProductCategorySerializer
from .serializers import ProductSerializer
from .serializers import CommentSerializer
from .serializers import ReplySerializer
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Q

from .models import *
from .forms import *


def get_product_queryset(query=None):
    queryset = []
    queries = query.split(' ')  # 백종원 도시락 => ['백종원', '도시락']
    for q in queries:
        products = Product.objects.filter(
            Q(name__icontains=q) |
            Q(description__icontains=q)
        ).distinct()

        for product in products:
            queryset.append(product)
    return list(set(queryset))


def index(request):
    query = ""
    title = "추천상품"
    if request.GET:
        query = request.GET['q']
        products = get_product_queryset(query)
        title = query + " 검색 결과"
    else:
        products = Product.objects.all()

    categories = Category.objects.all()
    return render(request, 'myside/index.html', {'title': title, 'products': products, 'categories': categories, 'query': query})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    categories = Category.objects.all()
    current_category = get_object_or_404(Category, slug=product.category)
    return render(request, 'myside/detail.html', {'product': product, 'categories': categories, 'current_category': current_category})


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
        'comment_form': comment_from,
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
        'reply_form': comment_from,
    }
    return render(request, 'myside/detail.html', context)


def product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True)
    title = "All Products"
    query = ""

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(
            category=current_category, available_display=True)
        title = current_category.name

    if request.GET:
        query = request.GET['q']
        products = get_product_queryset(query)
        title = query + " 검색 결과"

    return render(request, 'myside/list.html', {
        'current_category': current_category,
        'products': products,
        'categories': categories,
        'title': title,
        'query': query,
    })

def mymap(request):
    return render(request, 'myside/mymap.html', {
})


from django.views.generic import RedirectView

class ProductLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        id = self.kwargs.get('id')
        product = get_object_or_404(Product, id = id)
        url_ = product.get_absolute_url()
        user = self.request.user
        if user.is_authenticated:
            if user in product.like.all():
                product.like.remove(user)
            else:
                product.like.add(user)
        return url_




from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework import authentication, permissions

from .serializers import ReplySerializer
from .serializers import CommentSerializer
from .serializers import ProductSerializer
from .serializers import ProductCategorySerializer





class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'product-categories': reverse(ProductCategoryList.name, request=request),
            'products': reverse(ProductList.name, request=request),
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
    name = 'product-list'


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    name = 'product-detail'

class ProductLikeAPIToggle(APIView):
    authentication_classes  = [authentication.SessionAuthentication,]
    permission_classes      = [permissions.IsAuthenticated,]
    name = 'product_like-api-toggle'
    def get(self, request, pk=None, format=None):

        product = get_object_or_404(Product, pk=pk)
        url_ = product.get_absolute_url()
        user = self.request.user
        updated = False
        liked = False
        if user.is_authenticated:
            if user in product.like.all():
                liked = False
                product.like.remove(user)
            else:
                liked = True
                product.like.add(user)
            upudated = True
        data = {
            "updated": updated,
            "liked":liked,
        }
        return Response(data)

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-detail'


class ReplyList(generics.ListCreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    name = 'reply-list'


class ReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    name = 'reply-detail'
