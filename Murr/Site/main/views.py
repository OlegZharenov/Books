from django.shortcuts import render
from django.shortcuts import get_list_or_404
from django.shortcuts import redirect
from django.views.generic import View
from .utils import InfoMixin
from .forms import TagForm
from .models import *

class Posts(InfoMixin, View):
    Model = Post
    Template = 'main/main.html'


class Tags(InfoMixin, View):
    Model = Tag
    Template = 'main/tags.html'


class PostDetail(View):
    def post(request, slug):
        post = Post.objects.get(slug__iexact = slug)
        book = Book.objects.get(title = post.title)
        return render(request, 'main/post.html', context={'post': book})


class TagDetail(View):
    def tag(request, slug):
        tag = Tag.objects.get(slug__iexact = slug)
        posts = Post.objects.filter(genre = tag.title)
        return render(request, 'main/tag.html', context= {'posts':posts, 'tags':tag})


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'main/tag_create.html', context={'form':form})

    def post(self, request):
        form = TagForm(request.POST)
        if form.is_valid():
            new_tag = form.save()
            return redirect(new_tag)
        return render(request, 'main/tag_create.html', context={'form':form})
