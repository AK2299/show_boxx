from django.db import models
from django import forms

class Contact(models.Model):

    GENDER={
        ('male','male'),
        ('female','female'),
        ('others','others')
    }

    name=models.CharField(max_length=20)
    email=models.EmailField()
    gender=models.CharField(max_length=10, null=True,choices=GENDER)
