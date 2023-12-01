# models.py
from django.db import models
from django.utils import timezone

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    membership = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    created_datetime = models.DateTimeField(default=timezone.now)

class Contacts(models.Model):
    email = models.EmailField()