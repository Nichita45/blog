from django.shortcuts import render
from .models import Article, Author

def home(request):
    posts = Article.objects.all()
    context = {
        'posts': posts
    }
    return render(request, "article/home.html", context)

def contacts(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, "article/contacts.html", context)

def about(request):
    return render(request, "article/about.html")

def test(request):
    return render(request, "article/test.html")

def article_detail(request, slug):
    post = Article.objects.get(slug=slug)
    context = {
        "post": post
    }
    return render(request, "article/detail.html", context)

