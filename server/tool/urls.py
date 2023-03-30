from django.urls import path, re_path
from . import views

# 视图函数命名空间: 区分不同的应用
app_name = "tool"

urlpatterns = [
    re_path(r"^tool/",
            views.IndexView.as_view(),
            name="index"),
]
