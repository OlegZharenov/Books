from django.urls import path
from .views import *

urlpatterns = [
    path('', Posts.as_view(), name = 'main_url'),
    path('post/<slug>/', PostDetail.as_view(), name = 'post.url'),
    path('tags', Tags.as_view(), name = 'tags.url'),
    path('tags/tag/create', TagCreate.as_view(), name = 'tag_create.url'),
    path('tags/tag/<slug>/', TagDetail.as_view(), name = 'tag.url')
]