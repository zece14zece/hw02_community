from django.contrib import admin
from django.urls import include, path
from posts import views

posts_patterns = ([
    path('', views.index, name="index"),
    path('group/<slug:slug>/', views.group_posts, name='group_posts'),
], 'posts')

urlpatterns = [
    path('', include(posts_patterns)),
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),
]