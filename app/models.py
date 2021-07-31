from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.template.defaultfilters import truncatechars









#------------------------------------------------------------------------------
class Rom(models.Model):
    name = models.CharField(max_length=40)
    UUID = models.CharField(max_length=20)
    family_id = models.CharField(max_length=20)
    node_id = models.CharField(max_length=20)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField()

    def __str__(self):
        return self.UUID



#------------------------------------------------------------------------------
class Node1(models.Model):
    UUID = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    tamper = models.CharField(max_length=20)
    moves = models.CharField(max_length=20)
    resets = models.CharField(max_length=20)
    charger = models.CharField(max_length=20)
    USB = models.CharField(max_length=20)
    HMI = models.CharField(max_length=20)
    cpuTemp = models.CharField(max_length=20)
    created_on = models.DateTimeField()

    def __str__(self):
        return self.UUID



#------------------------------------------------------------------------------
class Temp12(models.Model):
    UUID = models.CharField(max_length=20)
    temp = models.CharField(max_length=20)
    created_on = models.DateTimeField()

    def __str__(self):
        return self.UUID



#------------------------------------------------------------------------------
class Gps2(models.Model):
    UUID = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    created_on = models.DateTimeField()

    def __str__(self):
        return self.UUID



#------------------------------------------------------------------------------
class Sd1(models.Model):
    UUID = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    period = models.CharField(max_length=20)
    capacity = models.CharField(max_length=20)
    free = models.CharField(max_length=20)
    cycles = models.CharField(max_length=20)
    created_on = models.DateTimeField()

    def __str__(self):
        return self.UUID



#------------------------------------------------------------------------------
class Modem1(models.Model):
    UUID = models.CharField(max_length=20)
    rssi = models.CharField(max_length=20)
    battery = models.CharField(max_length=20)
    updaterate = models.CharField(max_length=20)
    sent = models.CharField(max_length=20)
    lost = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    created_on = models.DateTimeField()

    def __str__(self):
        return self.UUID











# End
