# models.py
from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    membership = models.CharField(max_length=20)

class Contacts(models.Model):
    email = models.EmailField()