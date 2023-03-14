from django.urls import re_path

from . import views

app_name = "comment"
urlpatterns = [
    re_path(r"^comment/post/(?P<post_pk>[0-9]+)/$",
            views.post_comment,
            name="post_comment")
]
