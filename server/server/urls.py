"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from blog.feeds import AllPostsRssFeed
# from admin_site.admin import admin_site

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('admin/', admin_site.urls),

    path("", include("blog.urls")),
    path(r"", include("comment.urls")),
    re_path(r"^all/rss/$", AllPostsRssFeed(), name="rss"),
]
