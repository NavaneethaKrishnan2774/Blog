from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.template import loader
import logging
from .models import Post
from django.core.paginator import Paginator


def index(request):
    blog_title = 'kryzen tech'
    content = "Some quick example text for the post's content."

    all_posts = Post.objects.all()
    paginator = Paginator(all_posts,6)
    page_number= request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    return render(request,'index.html',{'blog_title': blog_title,'page_obj':page_obj})


def detail(request, slug):

    try:
        post = Post.objects.get(slug=slug)
        related_post= Post.objects.filter(category = post.category).exclude(pk=post.id)

    except Post.DoesNotExist:
        raise Http404("page doen not avail at the moment")

    return render( request,"detail.html",{"post": post ,"related_post":related_post})


def brief(request, post_id):
    return HttpResponse(f"brief content {post_id}")


def old_url(request):
    return redirect(reverse("blog:new_url"))


def new_url(request):
    return HttpResponse("this is our new url page")
