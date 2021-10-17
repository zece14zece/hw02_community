from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Group

def index(request):
    template: str = 'posts\index.html'
    posts: object = Post.objects.order_by('-pub_date')[:10]
    context: Dict[str, object] = {
        'posts': posts,
    }
    return render(request, template, context)

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
