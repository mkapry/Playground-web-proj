from django.conf.urls import url

from game.views import stats, game, total, CoursePage, GameCreateView
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path
from django.views.static import serve

app_name = 'game'

urlpatterns = [
    url('^stats/$', stats, name='stats'),
    url('^course/$', CoursePage.as_view(), name='course'),
    url('^total/$', total, name='total'),
    url('^add/$', GameCreateView.as_view(), name='game'),
    url('^$', game, name='game'),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]