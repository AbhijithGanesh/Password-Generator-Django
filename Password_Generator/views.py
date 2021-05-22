from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import RegistrationForm
from .models import *
import csv
from django.contrib.auth.models import User
from .Caller_Module import callerfile



def landing_page(request):
    return render(request, 'Password_Generator/HTML-JS-CSS/about.html')

def file_handling():
    _choices = list(Registration.objects.all())
    _RegisNames = []
    _RegisEmail = []
    _RegisContactNumber = []
    _RegisOrg = []
    _RegisCountry = []
    _Rows = []
    for i in range(len(_choices)):
        _RegisNames.append(_choices[i].Name)
        _RegisOrg.append(_choices[i].Email)
        _RegisEmail.append(_choices[i].Contact_Number)
        _RegisContactNumber.append(_choices[i].Organization)
        _RegisCountry.append(_choices[i].Country)
    for i in range(len(_RegisNames)):
        a = [_RegisNames[i], _RegisCountry[i], _RegisContactNumber[i], _RegisEmail[i], _RegisOrg[i]]
        _Rows.append(a)
    filename = 'Registrations.CSV'
    with open(filename, 'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(['Name', 'Email', 'Contact Number', 'Organization', 'Country'])
        csvwriter.writerows(_Rows)


def registration_form(request):
    form = RegistrationForm()
    if request.POST:
        form = RegistrationForm(data=request.POST)
        print(request.COOKIES)
        if form.is_valid():
            form.save()
            #user = User.objects.create_user()
            return redirect('redirection.html')
        else:
            form = RegistrationForm()
    return render(request, 'Password_Generator/HTML-JS-CSS/register.html', {'form': form})
    


def members(request):
    return render(request, 'Password_Generator/HTML-JS-CSS/members.html')


def redirection(request):
    return render(request,'Password_Generator/HTML-JS-CSS/Intermediate/redirection.html')

def Password(request):
    val = callerfile.password_Final()
    _val_1 = val[0:33]
    _val_2 = val[33:65]
    _val_3 = val[65:97]
    _val_4 = val[97:129]
    return render(request, 'Password_Generator/HTML-JS-CSS/Generator.html', {'password_1': _val_1,
                                                                             'password_2': _val_2,
                                                                             'password_3': _val_3,
                                                                             'password_4': _val_4, })
   
