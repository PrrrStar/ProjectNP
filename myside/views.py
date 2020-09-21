from .serializers import ProductCategorySerializer
from .serializers import ProductSerializer
from .serializers import CommentSerializer
from .serializers import ReplySerializer
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Q, Count

from .models import *
from .forms import *


def get_product_queryset(query=None, category_id = None):
    queryset = []
    queries = query.split(' ')  # 백종원 도시락 => ['백종원', '도시락']
    if category_id:
        for q in queries:   
            products = Product.objects.filter(
                    category=category_id
                ).filter(
                Q(name__icontains=q)|
                Q(description__icontains=q)|
                Q(brand__name=q)
            ).distinct()
            for product in products:
                queryset.append(product)
    else:
        for q in queries:   
            products = Product.objects.filter(
                Q(name__icontains=q)|
                Q(description__icontains=q)|
                Q(brand__name=q)
            ).distinct()
            for product in products:
                queryset.append(product)
    return list(set(queryset))



def index(request):
    query = ""
    title_all_product = "전체 상품"
    title_best_product = "베스트 상품"
    best_products = Product.objects.annotate(like_count=Count('like')).order_by('-like_count')
    products = Product.objects.all()
    categories = Category.objects.all()

    if request.GET:
        query = request.GET['q']
        products = get_product_queryset(query, None)
        title = "전체 상품 > "+query + " 검색 결과"
        context = {
            'title':title,
            'products':products,
            'categories':categories,
            'query':query,
        }
        return render(request, 'myside/list.html', context)

    context = {
        'title_all_product':title_all_product,
        'title_best_product':title_best_product,
        'products':products,
        'best_products':best_products,
        'categories':categories,
        'query':query,
    }
    return render(request, 'myside/index.html', context)

def product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True)
    title = ""
    query = ""

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(
            category=current_category, available_display=True)
        title = current_category.name
        if request.GET:
            query = request.GET['q']
            products = get_product_queryset(query, current_category)
            title = current_category.name+" > "+query + " 검색 결과"


    context = {
        'products':products,
        'title':title,
        'categories':categories,
        'current_category':current_category,
        'query':query,
    }
    return render(request, 'myside/list.html', context)

def product_detail(request, slug):
    product             = get_object_or_404(Product, slug=slug)
    categories          = Category.objects.all()
    current_category    = get_object_or_404(Category, slug=product.category)        
    context = {
            'product':product,
            'categories':categories,
            'current_category':current_category,
        }
    return render(request, 'myside/detail.html', context)

def product_tagged(request, slug):
    print("a)")
    tag                 = get_object_or_404(ProductTag, slug=slug)
    products            = Product.objects.filter(tags = tag)
    categories          = Category.objects.all()
    title               = tag.name + " 검색 결과"
    context = {
        'title':title,
        'tag':tag,
        'products':products,
        'categories':categories,
    }
    return render(request, 'myside/list.html',context)

def comment_create(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            author  = request.user
            if author.is_authenticated:
                content = request.POST.get('content')
                comment = Comment.objects.create(
                    product=product,
                    author =author, 
                    content=content
                    )
                comment.save()
            return HttpResponseRedirect(product.get_absolute_url())
    else:
        comment_from = CommentForm()

    context = {
        'comment_form': comment_from,
    }
    return render(request, 'myside/detail.html', context)




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
