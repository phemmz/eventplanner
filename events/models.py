from __future__ import unicode_literals
from django.db import models

# Create your models here.
class DefaultEvent(models.Model):
    event_category = models.CharField(max_length=250)
    event_description = models.CharField(max_length=500)
    event_image = models.FileField()

    def __str__(self):
        return self.event_description

class Event(models.Model):
    default_event = models.ForeignKey(DefaultEvent, on_delete=models.CASCADE)
    event_category = models.CharField(max_length=250)
    event_description = models.CharField(max_length=500)
    event_image = models.FileField()
    event_class = models.CharField(max_length=15, default='non-active')

    def __str__(self):
        return self.event_description
