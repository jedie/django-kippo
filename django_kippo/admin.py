# coding: utf-8

from django.contrib import admin

from django_kippo.models import Auth, Clients, Input, Sensors, Sessions, Ttylog


class AuthAdmin(admin.ModelAdmin):
    pass
admin.site.register(Auth, AuthAdmin)


class ClientsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Clients, ClientsAdmin)


class InputAdmin(admin.ModelAdmin):
    pass
admin.site.register(Input, InputAdmin)


class SensorsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Sensors, SensorsAdmin)


class SessionsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Sessions, SessionsAdmin)


class TtylogAdmin(admin.ModelAdmin):
    pass
admin.site.register(Ttylog, TtylogAdmin)

