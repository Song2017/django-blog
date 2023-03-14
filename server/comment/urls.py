from django.urls import re_path, include

#
# from . import views

# app_name = "comment"
urlpatterns = [
    re_path(r"^comment2/post/(?P<post_pk>[0-9]+)/$", include(""), name="post_comment")
]
