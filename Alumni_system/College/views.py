from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from Alumni_system.settings import reCAPTCHA_SECRET_KEY, reCAPTCHA_SITE_KEY
from Users.models import Colleges
import requests, json

def on_bording(request):
    return render(request, 'College/onboarding.html')

def college_home(request):
    return HttpResponse('College-home.')

def college_login(request):
    if request.method == 'POST':
        form = forms.CollegeLoginForm(request.POST)
        if form.is_valid():
            clg_name = form.cleaned_data['college_name']
            clg_code = form.cleaned_data['college_code']
            clg_pass = form.cleaned_data['college_pass']
            secret_key = reCAPTCHA_SECRET_KEY
            clint_key = request.POST['g-recaptcha-response']
            college = Colleges.college_manager.filter(clg_code = clg_code)
            data = {
                'response' : clint_key,
                'secret' : secret_key
            }
            resp = requests.post('https://www.google.com/recaptcha/api/siteverify', data = data)
            response = json.loads(resp.text)
            verify = response['success']
            for col in college:
                if col.college_pass == clg_pass and verify:
                    return redirect('college_home')
    form = forms.CollegeLoginForm()
    return render(request, 'College/college_login.html', context = {'form' : form})

