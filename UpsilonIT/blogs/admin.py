from .models import Blog, Post
from django.contrib import admin

class BlogAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)