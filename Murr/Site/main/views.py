from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Book


def main(request):
    posts = Post.objects.all()
    return render(request, 'main/main.html', context={'posts': posts})

def post(request, slug):
    post = Post.objects.get(slug__iexact = slug)
    book = Book.objects.get(title = post.title)
    return render(request, 'main/post.html', context={'post': book})

def tags(request, slug):
    pass
