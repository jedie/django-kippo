# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Auth(models.Model):
    id = models.IntegerField(primary_key=True)
    session = models.CharField(max_length=96)
    success = models.IntegerField()
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    timestamp = models.DateTimeField()
    class Meta:
        db_table = u'auth'

class Clients(models.Model):
    id = models.IntegerField(primary_key=True)
    version = models.CharField(max_length=150)
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

