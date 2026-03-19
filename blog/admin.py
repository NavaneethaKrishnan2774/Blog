from django.contrib import admin
from .models import Post , Category,Aboutus
# Register your models here.

class postadmin(admin.ModelAdmin):
    list_display=('title','content')
    list_filter =('category','created_at')
    search_fields =('title','content')
    prepopulated_fields = {'slug':('title',)}
admin.site.register(Post,postadmin)
admin.site.register(Category)
admin.site.register(Aboutus)