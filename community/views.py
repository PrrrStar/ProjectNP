from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect
from .models import *
from .forms import *
# Create your views here.


def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다')
    post.update_hits
    return render(request, 'community/post_detail.html', {'post': post})

def post_list(request):
    all_posts = Post.objects.prefetch_related('recommend').all().order_by('-id')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_posts, 5)

    posts = paginator.get_page(page)
    return render(request, 'community/post_list.html', {'posts': posts})

def post_write(request):
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
            recommend=Recommend()
            recommend.post=post
            recommend.save()
            return redirect('/community/list/')
    else:
        form = PostForm()
    return render(request, 'community/post_write.html', {'form': form})

def post_recommend(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    recommend=Recommend.objects.get(post=post)
    if user in recommend.user.all():
        recommend.user.remove(user)
        post.minus_recommend_count
    else:
        recommend.user.add(user)   
        post.plus_recommend_count
    return HttpResponseRedirect(post.get_absolute_url())

def comment_write(request, pk):
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
