from django.contrib import admin

# Register your models here.
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title", "created_time", "modified_time", "category", "author"
    ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "url", "text", "post"]


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
