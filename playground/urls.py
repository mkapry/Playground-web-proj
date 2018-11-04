from django.conf.urls import url
from django.contrib import admin
from django.urls import include, re_path
from playground.views import BlogList, BlogCreate, PostCreate, CommentCreate, PostList, CommentList, welcome, \
    PostUpdate, CommentUpdate, BlogUpdate, PostLikeAjaxView, SearchView
from django.contrib.auth.decorators import login_required
from playground.views import *
from jsonrpc import jsonrpc_site




urlpatterns = [
    url(r'^blogs/$', BlogList.as_view(), name="blog_list"),
    re_path(r'^api/', jsonrpc_site.dispatch, name='jsonrpc_mountpoint'),
    url(r'^blogs/(?P<pk>\d+)/$', PostList.as_view(), name="blog_page"),
    url(r'^create/$', login_required(BlogCreate.as_view()), name="blog_create"),
    url(r'^postpage/(?P<pk>\d+)/$', CommentList.as_view(), name="post_page"),
    url(r'^createcomment/(?P<pk>\d+)/$', login_required(CommentCreate.as_view()), name="comment_create"),
    url(r'^createpost/(?P<pk>\d+)/$', login_required(PostCreate.as_view()), name="post_create"),
    #url(r'^welcome/', welcome),
    url(r'^updatepost/(?P<pk>\d+)$', login_required(PostUpdate.as_view()), name="post_update"),
    url(r'^updateblog/(?P<pk>\d+)/$', login_required(BlogUpdate.as_view()), name="blog_update"),
    url(r'^updatecomment/(?P<pk>\d+)/$', login_required(CommentUpdate.as_view()), name="comment_update"),
    url(r'^likes/(?P<pk>\d+)/$', PostLikeAjaxView.as_view(), name="likes"),
    url(r'^search_post/$', SearchView.as_view(), name="search_post"),
    url(r'^welcome/', include('social_django.urls')),
    url(r'^welcome2/', my_view, name="welcome"),
]