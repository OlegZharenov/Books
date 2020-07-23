from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'main_url'),
    path('post/<slug>/', views.post, name = 'post.url'),
    path('tags', views.tags, name = 'tags.url')
]