from .models import Blog, Post

total_blogs = None


def overall_stats(request):
    result = {'total_posts' : Post.objects.count()}

    global total_blogs
    if total_blogs is None:
        total_blogs = Blog.objects.count()

    result['total_blogs'] = total_blogs
    return result
