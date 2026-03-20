from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.template import loader
import logging
from .models import Post ,Aboutus
from django.core.paginator import Paginator
from .forms import contactform, loginform , registerform
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login

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
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        logger = logging.getLogger('TEST')
        if form.is_valid():
            logger.debug(f"data is{form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}")
            success_message ='The message has been submitted successfully'
            return render(request,"contact.html",{'form':form,'success_message':success_message})

        else:
            logger.debug("data validation is failed")
        return render(request,"contact.html",{'form':form,'name':name,'email':email,'message':message})
    return render(request,"contact.html")

def about(request):
    about_content = Aboutus.objects.first()
    if about_content is None or not  about_content.content:
        about_content='The default content is here'
    else:
        about_content=about_content.content
    return render(request,'about.html',{'about_content':about_content})
 
def user_login(request):
    form = loginform()
    if request.method=='POST':
        form = loginform(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                auth_login(request,user)
                print("login successed")
                return redirect("/dashboard")
            
    return render(request,'login.html',{'form':form})

def register(request):
    form =  registerform()
    if request.method == 'POST':
        form = registerform(request.POST)
        if form.is_valid():
            user=form.save(commit=False)#create user data
            user.set_password(form.cleaned_data['password'])
            user.save()
            print("registered successfully")
            messages.success(request,"registered successfully")
        
            
    return render(request,'register.html',{'form':form})
 

def forgot_password(request):
    return render(request,'forgot_password.html.html')

def reset_password(request):
    return render(request,'reset_password.html.html')

def reset_password_email(request):
    return render(request,'reset_password_email.html')

def edit_post(request):
    return render(request,'edit_post.html')

def new_post(request):
    return render(request,'new_post.html')

