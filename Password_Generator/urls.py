
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', landing_page,),
    path('about.html',landing_page),
    #path('register.html',register),
    path('members.html',members),
    path('register.html', registration_form),
    path('redirection.html',redirection),
    path('Password.html',Password),
]
