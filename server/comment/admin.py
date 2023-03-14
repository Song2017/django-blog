from django.contrib import admin

# Register your models here.
from .models import *


class CommentAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "url", "text", "post"]


admin.site.register(Comment, CommentAdmin)