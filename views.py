from django.shortcuts import render,redirect
from .forms import *
from .models import Contact
from django.contrib.messages.api import success
from django.contrib import messages

def show(request):
     
     return render( request,'pro.html')
