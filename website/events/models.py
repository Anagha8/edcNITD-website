from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

class Event(models.Model):
    event_name=models.CharField(max_length=100)
    about_event=models.TextField(max_length=2000)
    rules=models.TextField(max_length=2000,default="",blank=True,null=False)
    poster=models.ImageField(upload_to=None, default="",blank=True,null=False)
    start_date=models.DateTimeField(auto_now=False,auto_now_add=False,blank=True,null=True)
    end_date=models.DateTimeField(auto_now=False,auto_now_add=False,blank=True,null=True)
    registration_link=models.URLField(blank=True,null=True)
    
    def __str__(self):
        return self.event_name

class EventImages(models.Model):
    event=models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    images=models.FileField(upload_to='images/')

    def __str__(self):
        return self.event.event_name

class Timeline(models.Model):
    event=models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    details=models.CharField(max_length=300)

    def __str__(self):
        return self.event.event_name

