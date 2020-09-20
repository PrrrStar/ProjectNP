from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404
from .models import Post, Recommend
from .forms import *
# Create your views here.


def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다')
    post.update_hits
    return render(request, 'community/post_detail.html', {'post': post})


#def post_write(request):
    

def post_list(request):
    all_posts = Post.objects.prefetch_related('recommend').all().order_by('-id')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_posts, 5)

    posts = paginator.get_page(page)
    return render(request, 'community/post_list.html', {'posts': posts})

def post_write(request):
    if not request.session.get('user'):
         return redirect('/')
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post()
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('/community/list/')
    else:
        form = PostForm()
    return render(request, 'community/post_write.html', {'form': form})

def post_recommend(request, pk):
    post = Post.objects.get(pk=pk)
    recommend=Recommend.objects.get(post=post)
    if request.user in recommend.user.all():
        recommend.user.remove(request.user)
        post.minus_recommend_count
    else:
        recommend.user.add(request.user)   
        post.plus_recommend_count
    return redirect('/community/list/')