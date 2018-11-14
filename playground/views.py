from django.db import models
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from jsonrpc import jsonrpc_method
from jsonrpc.exceptions import Error
from django.core.serializers import serialize
import json
from django.shortcuts import redirect, render

# Create your views here.
from django.views import View
from django.views.generic import ListView, CreateView, TemplateView
from django.views.generic.edit import UpdateView

# from playground.forms import BlogCreate, CommentCreate, PostCreate
from playground.forms import PostCreateForm, SearchForm, BlogCreateForm, CommentCreateForm
from playground.models import Blog, Comment, Post, Like
from core.models import User
from django.contrib.auth import authenticate, login, logout


class BlogList(ListView):
    template_name = "playground/blog_list.html"
    model = Blog
    fields = ('name', 'author')

    @jsonrpc_method('playground.get_blog')
    def get_blog(request):
        return json.loads(serialize('json', Blog.objects.all()))


class BlogCreate(CreateView):
    template_name = "playground/create_blog.html"
    model = Blog
    # form_class = BlogCreate
    fields = ('name', 'author')

    def get_success_url(self):
        return '/'

    @jsonrpc_method('playground.add_blog')
    def add_blog(request, **kargs):
        name = kargs.get('name', None)
        if name is None:
            raise Error('No "name" field')

        user = kargs.get('user', None)
        if user is None:
            raise Error('No "user" field')
        user = User.objects.filter(username=user).first()
        form = BlogCreateForm(kargs)
        print( kargs, form.is_valid(), form, user, User.objects.all() )
        #blog = Blog.objects.filter(author=request.user, name=name).exsists()
        blog = Blog.objects.filter(author=user, name=name).exists()
        if blog is not False:
            raise Error('The blog already exists')
        form.save()
        print( Blog.objects.all() )
        return "success"


class CommentCreate(CreateView):
    template_name = "playground/create_comment.html"
    model = Comment
    # form_class = CommentCreate
    fields = ('text', 'author', 'post')

    def get_success_url(self):
        return '/'

    def form_valid(self, form):
        result = super(CommentCreate, self).form_valid(form)
        Post.objects.filter(pk=self.object.post.pk).update(
            comment_count=models.F('comment_count') + 1
        )
        return result

    @jsonrpc_method('playground.add_comment')
    def add_comment(request, **kargs):
        text = kargs.get('text', None)
        if text is None:
            raise Error('No "text" field')

        user = kargs.get('user', None)
        if user is None:
            raise Error('No "user" field')
        user = User.objects.filter(username=user).first()
        form = CommentCreateForm(kargs)
        print(dir(form), form.is_valid())
        # blog = Blog.objects.filter(author=request.user, name=name).exsists()
        comment = Comment.objects.filter(author=user, text=text).exists()
        if comment is not False:
            raise Error('The comment already exists')
        form.save()
        return "success"


class PostCreate(CreateView):
    template_name = "playground/create_post.html"
    # model = Post
    # fields = ('blog', 'author', 'text')
    form_class = PostCreateForm

    def get_success_url(self):
        return '/'

    @jsonrpc_method('playground.add_post')
    def add_post(request, **kargs):
        text = kargs.get('text', None)
        if text is None:
            raise Error('No "text" field')

        user = kargs.get('user', None)
        if user is None:
            raise Error('No "user" field')
        user = User.objects.filter(username=user).first()
        form = PostCreateForm(kargs)
        print(dir(form), form.is_valid())
        # blog = Blog.objects.filter(author=request.user, name=name).exsists()
        post = Post.objects.filter(author=user, text=text).exists()
        if post is not False:
            raise Error('The post already exists')
        form.save()
        return "success"


class PostList(ListView):
    template_name = "playground/blog_page.html"
    model = Post
    fields = ('blog', 'author', 'text')

    def dispatch(self, request, *args, **kwargs):
        self.blog = Blog.objects.get(pk=kwargs['pk'])

        return super(PostList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = super(PostList, self).get_queryset()
        qs = qs.filter(blog=self.blog)

        return qs

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['blog'] = self.blog
        return context

    @jsonrpc_method('playground.get_posts')
    def get_posts(request):
        return json.loads(serialize('json', Post.objects.all()))


class CommentList(ListView):
    template_name = "playground/post_page.html"
    model = Comment
    fields = ('post', 'author', 'text')

    def dispatch(self, request, *args, **kwargs):
        self.post = Post.objects.get(pk=kwargs['pk'])

        return super(CommentList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = super(CommentList, self).get_queryset()
        qs = qs.filter(post=self.post)

        return qs

    def get_context_data(self, **kwargs):
        context = super(CommentList, self).get_context_data(**kwargs)
        context['post'] = self.post
        return context

    @jsonrpc_method('playground.get_comment')
    def get_comment(request):
        return json.loads(serialize('json', Comment.objects.all()))


class BlogUpdate(UpdateView):
    template_name = "playground/blogupdate.html"
    model = Blog
    fields = ['name']

    def get_success_url(self):
        return '/'

    @jsonrpc_method('playground.upd_blog')
    def upd_blog(request, **kargs):
        name = kargs.get('name', None)
        if name is None:
            raise Error('No "name" field')
        id = kargs.get('id', None)
        if id is None:
            raise Error('No "id" field')
        user = kargs.get('user', None)
        if user is None:
            raise Error('No "user" field')
        user = User.objects.filter(username=user).first()
        blog = Blog.objects.filter(id=id).exists()
        if blog is False:
            raise Error('The blog doesnt exist')
        else:
            blog = Blog.objects.filter(id=id).first()
            form = BlogCreateForm(kargs, instance=blog)
            form.save()
        return "success"


class PostUpdate(UpdateView):
    template_name = "playground/post_update.html"
    model = Post
    fields = ['text']

    def get_success_url(self):
        return '/'


class CommentUpdate(UpdateView):
    template_name = "playground/comment_update.html"
    model = Comment
    fields = ['text']

    def get_success_url(self):
        return '/'


def welcome(request):
    if request.user.is_authenticated:
        return render(request, 'playground/base.html')


class PostLikeAjaxView(View):

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.post_object = get_object_or_404(Post, id=pk)
        return super(PostLikeAjaxView, self).dispatch(request, *args, **kwargs)

    def post(self):
        if not self.post_object.likes.filter(user=self.request.user).exists():
            return HttpResponse(Like.objects.filter(post=self.post_object).count())


class SearchView(TemplateView):
    template_name = 'playground/search_post.html'

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)

        query = self.request.GET.get('search') or ''
        # import pdb; pdb.set_trace()
        context['object_list'] = Post.objects.filter(text__icontains=query)
        context['form'] = SearchForm(self.request.GET)

        return context


def my_view(request):
    print( request.user )
    #logout(request)
    return render(request, 'playground/welcome.html')