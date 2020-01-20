from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
import json
import requests
from .models import Alumni_User
from Alumni_system.settings import reCAPTCHA_SECRET_KEY

def on_bording(request):
    return render(request, 'Users/onboarding.html')


def user_dashboard(request):
    return HttpResponse("User DashBoard Page.")

def register(request):
    
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            # user = form.save()
            # user.set_password(user.password)
            form.save()
            return redirect('/user-login/')
    
    else:
        form = forms.RegistrationForm()
    return render(request, 'Users/register.html', context = {'form' : form})

def login(request):
    if request.method == 'POST':
        form = forms.LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            secret_key = reCAPTCHA_SECRET_KEY
            clint_key = request.POST['g-recaptcha-response']
            print(email, password)
            user = Alumni_User.alumni.filter(email = email)
            #for u in user:
                #if u.password == password:

            # captcha verification.
            data = {
                'response' : clint_key,
                'secret' : secret_key
            }
            resp = requests.post('https://www.google.com/recaptcha/api/siteverify', data = data)
            response = json.loads(resp.text)
            verify = response['success']

            print('Your success is: ', verify)

            if verify:
                return redirect('/dashboard-user/')
            
    form = forms.LogInForm()
    return render(request, 'Users/login.html', context = {'form' : form })
