from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Classify(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object = models.CharField(max_length=100)
    content_object = GenericForeignKey('content_type', 'object')


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object = models.IntegerField(default=0)
    content_object = GenericForeignKey('content_type', 'object')


class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    classif = GenericRelation(Classify)

    def __str__(self):
        return self.name

    @property
    def classify(self):
        return self.classif.value_from_object()


class PostQuerySet(models.QuerySet):

    def aggregate_comments(self):

        return self.annotate(comments_count=models.Count('comment_id'))

    def available_for_user(self, user):

        return self.filter(models.Q(is_deleted=False) | models.Q(author=user))


class Post(models.Model):
    text = models.TextField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    likes = GenericRelation(Like, object_id_field='object')
    is_deleted = models.BooleanField(default=False)
    comment_count = models.IntegerField(default=0)

    objects = PostQuerySet.as_manager()

    @property
    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField(default=0)



