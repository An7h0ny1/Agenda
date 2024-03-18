from django.db import models
from datetime import date
from schedule.models import Event

# Create your models here.

class Todo(models.Model):
    imagen = models.ImageField(upload_to='images/', blank=True, null=True)  # nuevo campo
    title = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField(blank=True)
    date = models.DateField(default=date.today , auto_now=False, auto_now_add=False)
    estimated_end = models.DateField(blank=True)
    priority = models.IntegerField(default=3)
   

    def __str__(self):
        return self.title

class MyEvent(Event):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)