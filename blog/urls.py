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
    path("about/",views.about,name="about")
    ]