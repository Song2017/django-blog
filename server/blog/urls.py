from django.urls import path, re_path
from . import views

# 视图函数命名空间: 区分不同的应用
app_name = "blog"

urlpatterns = [
    path(r"", views.IndexView.as_view(), name="index"),
    re_path(r"^post/(?P<pk>[0-9]+)/$",
            views.PostDetailView.as_view(),
            name="detail"),
    re_path(
        r"^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$",
        views.ArchivesView.as_view(),
        name="archives",
    ),
    re_path(r"^category/(?P<pk>[0-9]+)/$",
            views.CategoryView.as_view(),
            name="category"),
    re_path(r"^tag/(?P<pk>[0-9]+)/$", views.TagView.as_view(), name="tag"),

    re_path(r"^comment/post/(?P<post_pk>[0-9]+)/$",
            views.post_comment,
            name="post_comment"),
]
