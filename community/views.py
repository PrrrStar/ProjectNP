from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404
from .models import Post
# Create your views here.


def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다')
    post.update_counter
    return render(request, 'community/post_detail.html', {'post': post})


#def post_write(request):
    

def post_list(request):
    all_posts = Post.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_posts, 5)

    posts = paginator.get_page(page)
    return render(request, 'community/post_list.html', {'posts': posts})
