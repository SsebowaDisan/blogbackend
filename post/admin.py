from django.contrib import admin
from .models import Post, Views_Post, Comment_Post

admin.site.register(Post)
admin.site.register(Comment_Post)
admin.site.register(Views_Post)
