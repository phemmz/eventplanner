from django.contrib import admin

# Register your models here.
from .models import DefaultEvent, Event

admin.site.register(DefaultEvent)
admin.site.register(Event)