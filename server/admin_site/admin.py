from django.contrib import admin
from django.utils.translation import gettext_lazy


class MyAdminSite(admin.AdminSite):
    site_header = gettext_lazy("admin page")
