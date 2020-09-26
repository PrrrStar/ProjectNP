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


def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
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
        if str(pk) not in cookies_list:
            response.set_cookie(cookie_name, cookies + f'|{pk}', expires =expires)
            post.update_hits
            return response
    else:
        response.set_cookie(cookie_name, pk, expires =expires)
        post.update_hits
        return response

    return render(request, 'community/post_detail.html', context)



def post_list(request):
    sort = request.GET.get('sort','')
    if sort == 'recommends':
        posts = Post.objects.annotate(recommends_count=Count('recommend_count')).order_by('-recommend_count', '-created_at')
    elif sort == 'hits':
        posts = Post.objects.order_by('-hits', '-created_at')
    elif sort == 'comments':
        posts = Post.objects.annotate(comment_count=Count('comment')).order_by('-comment_count', '-created_at')
    else :
        posts = Post.objects.order_by('-created_at')
    return render(request, 'community/post_list.html', {'posts': posts})

@login_required
@require_POST
def post_recommend(request):
    pk = request.POST.get('pk', None)
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    if user in post.recommends.all():
        post.recommends.remove(user)
        message = '추천 취소'
    else:
        post.recommends.add(user)
        message = '추천'

    context = {'recommends_count':post.recommends.count(), 'message': message}
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

def comment_create(request, pk):
    author = request.user
    post = Post.objects.get(pk=pk)
    if not author.is_authenticated:
        return redirect('/')    
    elif request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = Comment()
            comment.content = comment_form.cleaned_data['content']
            comment.author = author
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()
    return HttpResponseRedirect(post.get_absolute_url())
