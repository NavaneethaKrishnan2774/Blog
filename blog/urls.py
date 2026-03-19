from django.urls import path
from . import views
app_name="blog"
urlpatterns=[
    path("", views.index, name="home"),
    path("index/",views.index,name="index"),
    path("detail/<str:slug>/",views.detail,name="detail"),
    path("brief/<str:post_id>",views.brief,name="brief"),
    path("new_something_url/",views.new_url,name="new_url"),
    path("old_url/",views.old_url,name="old_url"),
    path("contact/",views.contact,name="contact"),
    path("about/",views.about,name="about"),
    path("login/",views.login,name='login'),
    path("register/",views.register,name='register'),
    path("forgotpassword/",views.forgot_password,name='forgotpassword'),
    path("resetpassword/",views.reset_password,name='resetpassword'),
    path("resetpasswordemail/",views.reset_password_email,name='resetpasswordemail'),
    path("newpost/",views.new_post,name='newpost'),
    path("editpost/",views.edit_post,name='editpost'),
    
    ]