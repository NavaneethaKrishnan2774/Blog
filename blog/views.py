from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.template import loader
import logging
from .models import Post
from django.core.paginator import Paginator
from .forms import contactform


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

def contact(request):
    if request.method =='POST':
        form = contactform(request.POST)
        logger = logging.getLogger('TEST')
        if form.is_valid():
            logger.debug(f"data is{form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}")
        else:
            logger.debug("data validation is failed")
        return render(request,"contact.html",{'form':form})
    return render(request,"contact.html")
