from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404
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


#def post_write(request):
    

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
            post.author=request.user
            post.save()
            recommend=Recommend()
            recommend.post=post
            recommend.save()
            return redirect('/community/list/')
    else:
        form = PostForm()
    return render(request, 'community/post_write.html', {'form': form})

@login_required
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
    return redirect('/community/list/')