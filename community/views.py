import json
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect, HttpResponse, JsonResponse
from django.db.models import Count
from .models import *
from .forms import *
# Create your views here.


def post_detail(request, post_pk):
    try:
        post = Post.objects.get(pk=post_pk)
    except Post.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다')
    context={'post': post}
    response= render(request, 'community/post_detail.html', context)
    
    if request.session.get('authUser') is None:
        cookie_name = 'hit'
    else:
        cookie_name = f'hit:{request.session["authUser"]["id"]}'

    tomorrow = datetime.datetime.replace(datetime.datetime.now(), hour=23, minute=59, second=0)
    expires = datetime.datetime.strftime(tomorrow, "%a, %d-%b-%Y %H:%M:%S GMT")

    if request.COOKIES.get(cookie_name) is not None:
        
        cookies = request.COOKIES.get(cookie_name)
        cookies_list = cookies.split('|')
        if str(post_pk) not in cookies_list:
            response.set_cookie(cookie_name, cookies + f'|{post_pk}', expires =expires)
            post.update_hits
            return response
    else:
        response.set_cookie(cookie_name, post_pk, expires =expires)
        post.update_hits
        return response

    return render(request, 'community/post_detail.html', context)

def post_list(request):
    sort = request.GET.get('sort','')
    if sort == 'recommends':
        posts = Post.objects.annotate(recommends_count=Count('recommends')).order_by('-recommends', '-created_at')
    elif sort == 'hits':
        posts = Post.objects.order_by('-hits', '-created_at')
    elif sort == 'comments':
        posts = Post.objects.annotate(comment_count=Count('comment')).order_by('-comment_count', '-created_at')
    else :
        posts = Post.objects.order_by('-created_at')
    return render(request, 'community/post_list.html', {'posts': posts})

@login_required
@require_POST
def post_recommend(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    user = request.user

    if user in post.recommends.all():
        post.recommends.remove(user)
        message = '추천 취소'
    else:
        post.recommends.add(user)
        message = '추천'

    context = {'recommends_count':post.recommends.count(), 'message': message}
    return HttpResponse(json.dumps(context), content_type="application/json")   

@login_required
@require_POST
def post_derecommend(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    user = request.user

    if user in post.derecommends.all():
        post.derecommends.remove(user)
        message = '반대 취소'
    else:
        post.derecommends.add(user)
        message = '반대'

    context = {'derecommends_count':post.derecommends.count(), 'message': message}
    return HttpResponse(json.dumps(context), content_type="application/json")  

def post_create(request):
    if not request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post()
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.author = request.user
            post.save()
            return redirect('/community/list/')
    else:
        form = PostForm()
    return render(request, 'community/post_create.html', {'form': form})

def post_delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    post.delete()
    return redirect('/community/list/')


def post_comment_create(request, post_pk):
    author = request.user
    post = Post.objects.get(pk=post_pk)
    if not author.is_authenticated:
        return redirect('/')    
    elif request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = PostComment()
            comment.content = comment_form.cleaned_data['content']
            comment.author = author
            comment.post = post
            comment.save()
            return redirect('post_detail', post_pk=post.pk)
    else:
        comment_form = CommentForm()
    return HttpResponseRedirect(post.get_absolute_url())

@require_POST
def post_comment_delete(request, post_pk, comment_pk):
    comment = get_object_or_404(PostComment, pk=comment_pk)
    post = get_object_or_404(Post, pk=post_pk)
    user= request.user
    if user.is_authenticated and user==comment.author: 
        comment.delete()
        message = '댓글 삭제'            
    context={'message': message}
    return HttpResponse(json.dumps(context), content_type="application/json")     
    


from rest_framework.views import APIView
from rest_framework import generics
from .serializers import *

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-list'

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'
    name = 'post-detail'

class PostCommentList(generics.ListCreateAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
    name = 'post-comment-list'

class PostCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
    lookup_field = 'id'
    name = 'post-comment-detail'