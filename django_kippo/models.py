# coding: utf-8

from django.db import models


class Auth(models.Model):
    id = models.IntegerField(primary_key=True)
    session = models.CharField(max_length=96)
    success = models.IntegerField()
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    timestamp = models.DateTimeField()

    def __unicode__(self):
        result = u"Kippo Auth [%s/%s]" % (self.username, self.password)
        if self.success == 1:
            result += " successfully."
        else:
            result += " failed."
        return result

    class Meta:
        db_table = u'auth'
        ordering = ('-timestamp',)

class Clients(models.Model):
    id = models.IntegerField(primary_key=True)
    version = models.CharField(max_length=150)

    def __unicode__(self):
        return "Client '%s'" % self.version

    class Meta:
        db_table = u'clients'


class Input(models.Model):
    id = models.IntegerField(primary_key=True)
    session = models.CharField(max_length=96)
    timestamp = models.DateTimeField()
    realm = models.CharField(max_length=150, blank=True)
    success = models.IntegerField(null=True, blank=True)
    input = models.TextField()
    class Meta:
        db_table = u'input'


class Sensors(models.Model):
    id = models.IntegerField(primary_key=True)
    ip = models.CharField(max_length=45)
    def __unicode__(self):
        return "IP: %s" % self.ip
    class Meta:
        db_table = u'sensors'


class Sessions(models.Model):
    id = models.CharField(max_length=96, primary_key=True)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField(null=True, blank=True)
    sensor = models.IntegerField()
    ip = models.CharField(max_length=45)
    termsize = models.CharField(max_length=21, blank=True)
    client = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'sessions'


class Ttylog(models.Model):
    id = models.IntegerField(primary_key=True)
    session = models.CharField(max_length=96)
    ttylog = models.TextField()
    class Meta:
        db_table = u'ttylog'

