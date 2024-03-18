from django.db import models
from datetime import date

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=True, null=False)
    mobile = models.CharField(max_length=12,  blank=False, null=False)
    email = models.EmailField()
    company = models.CharField(max_length=20,  blank=True)
    date = models.DateField(default=date.today,auto_now=False, auto_now_add=False)
    notes = models.TextField( blank=True)

    def __str__(self):
        return self.name

