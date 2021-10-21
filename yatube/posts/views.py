from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    template: str = 'posts/index.html'
    posts: object = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
