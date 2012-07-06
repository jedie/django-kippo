# coding: utf-8

from django.contrib import admin

from django_kippo.models import Auth, Client, Input, Sensor, Session, Ttylog
from django.conf import settings


class AuthAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "password", "success", "timestamp")
    list_display_links = ("username", "password")
    list_filter = ("session",)
    date_hierarchy = 'timestamp'
    search_fields = ("username", "password")
admin.site.register(Auth, AuthAdmin)


class InputAdmin(admin.ModelAdmin):
    list_display = ("id", "realm", "input", "success", "timestamp")
    list_display_links = ("id",)
    list_filter = ("session",)
    date_hierarchy = 'timestamp'
    search_fields = ("input",)
admin.site.register(Input, InputAdmin)


class SessionAdmin(admin.ModelAdmin):
    list_display = ("id", "ip", "starttime", "endtime", "termsize", "client")
    list_display_links = ("ip",)
    list_filter = ("ip", "client")
    date_hierarchy = "starttime"
    search_fields = ("ip", "client")
admin.site.register(Session, SessionAdmin)


class TtylogAdmin(admin.ModelAdmin):
    pass
admin.site.register(Ttylog, TtylogAdmin)


if getattr(settings, "ADD_ALL_KIPPO_MODELS", False):
    class SensorAdmin(admin.ModelAdmin):
        list_display = ("id", "ip")
        list_display_links = ("ip",)
        search_fields = ("ip",)
    admin.site.register(Sensor, SensorAdmin)

    class ClientAdmin(admin.ModelAdmin):
        list_display = ("version",)
    admin.site.register(Client, ClientAdmin)
