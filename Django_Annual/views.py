from django.shortcuts import render, redirect
from django.http import HttpResponse
#from .forms import RegistrationForm

def Landing(request):
    return render(request,'APP/Landing_Page.html')


def Land(request):
    return render(request,'APP/index.html')