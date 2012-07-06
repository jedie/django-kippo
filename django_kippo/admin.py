# coding: utf-8

from django.contrib import admin

from django_kippo.models import Auth, Clients, Input, Sensors, Sessions, Ttylog


class AuthAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "password", "success", "timestamp")
    list_display_links = ("username", "password")
    list_filter = ("session",)
    date_hierarchy = 'timestamp'
    search_fields = ("username", "password")
admin.site.register(Auth, AuthAdmin)


class ClientsAdmin(admin.ModelAdmin):
    list_display = ("version",)
admin.site.register(Clients, ClientsAdmin)


class InputAdmin(admin.ModelAdmin):
    list_display = ("id", "realm", "input", "success", "timestamp")
    list_display_links = ("id",)
    list_filter = ("session",)
    date_hierarchy = 'timestamp'
    search_fields = ("input",)
admin.site.register(Input, InputAdmin)


class SensorsAdmin(admin.ModelAdmin):
    list_display = ("id", "ip")
    list_display_links = ("ip",)
    search_fields = ("ip",)
admin.site.register(Sensors, SensorsAdmin)


class SessionsAdmin(admin.ModelAdmin):
    list_display = ("id", "ip", "starttime", "endtime", "termsize", "client")
    list_display_links = ("ip",)
    list_filter = ("ip", "client")
    date_hierarchy = "starttime"
    search_fields = ("ip", "client")
admin.site.register(Sessions, SessionsAdmin)


class TtylogAdmin(admin.ModelAdmin):
    pass
admin.site.register(Ttylog, TtylogAdmin)

