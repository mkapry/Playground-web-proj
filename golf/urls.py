"""golf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.contrib.auth.views import login, logout

from core import views
from core.views import UserPage
from golf import settings

urlpatterns = [
    url('^', include('game.urls', namespace='games')),
    url('^admin/', admin.site.urls),
    url('^accounts/profile/', UserPage.as_view()),
    url(r'^login/', login, {'template_name': 'core/login.html'}, name="login"),
    url(r'^logout/', logout, {'template_name': 'core/logout.html'}, name="logout"),
    url('^', include('playground.urls')),
    url(r'^signup/$', views.signup, name='signup'),

   # url(r'^/', , {'template_name': 'core/base.html'}, name="base"),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns