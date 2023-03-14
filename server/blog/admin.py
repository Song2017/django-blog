from django.contrib import admin

# Register your models here.
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title", "created_time", "modified_time", "category", "author"
    ]


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
