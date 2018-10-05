from django.contrib import admin

# Register your models here.
from .models import Post, Comment, Blog, Like

admin.site.register(Post)
admin.site.register(Blog)
admin.site.register(Like)
admin.site.register(Comment)
