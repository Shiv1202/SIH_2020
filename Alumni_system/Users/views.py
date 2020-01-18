from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from . import forms
import json
import requests
from .models import Alumni_User
from Alumni_system.settings import reCAPTCHA_SECRET_KEY

def on_bording(request):
    return render(request, 'Users/onboarding.html')


# Create your views here.
def home(request):
    return HttpResponse("Home Page.")

def register(request):
    
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            # user = form.save()
            # user.set_password(user.password)
            form.save()
            return redirect('login')
    
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
            #user = Alumni_User.objects.filter(email = email)

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
                return redirect('user-homepage')
            else:
                return render(request, 'Users/login.html', context = {'form' : form})
    else:
        form = forms.LogInForm()
        return render(request, 'Users/login.html', context = {'form' : form })
