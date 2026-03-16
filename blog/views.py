from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.template import loader
import logging
from .models import Post


def index(request):
    blog_title = 'kryzen tech'
    content = "Some quick example text for the post's content."

    posts = Post.objects.all()

    return render(
        request,
        'index.html',
        {
            'blog_title': blog_title,
            'content': content,
            'postcontent': posts
        }
    )


def detail(request, slug):

    try:
        posts = Post.objects.get(slug=slug)

    except Post.DoesNotExist:
        raise Http404("page doen not avail at the moment")

    return render(
        request,
        "detail.html",
        {"post": posts}
    )


def brief(request, post_id):
    return HttpResponse(f"brief content {post_id}")


def old_url(request):
    return redirect(reverse("blog:new_url"))


def new_url(request):
    return HttpResponse("this is our new url page")
