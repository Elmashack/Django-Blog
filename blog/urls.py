from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('category/<str:slug>/', PostsByCat.as_view(), name='category'),
    path('post/<str:slug>/', SinglePost.as_view(), name='post'),
    path('tag/<str:slug>/', PostByTag.as_view(), name='tag'),
    path('search/', SearchPost.as_view(), name='search'),
]
