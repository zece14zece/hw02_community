from django.urls import path

from . import views

app_name = 'main_page'

urlpatterns = [
    path('', views.index),
    path('posts/', views.index, name='main_page'),
    path('group/<slug:slug>/', views.group_posts, name='group_posts'),
]
