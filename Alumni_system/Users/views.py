from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from . import forms
import json
import requests
from .models import Alumni_User
from .tokens import account_activation_token
from django.contrib.auth.hashers import make_password
from Alumni_system.settings import reCAPTCHA_SECRET_KEY
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.mail import send_mail

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
            #user12.password=make_password(user12.password,None, 'md5')
            user12 = form.save(commit=False)
            user12.password=make_password(user12.password)
            user12.is_active = False
            user12.save()
            current_site = get_current_site(request)
            message = render_to_string('Users/acc_active_email.html', {
                'user':user12, 'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user12.pk)),
                'token': account_activation_token.make_token(user12),
            })
            mail_subject = 'Activate your blog account.'
            # from_email = ['teamrachnatmaksih2020@gmail.com']
            to_email = form.cleaned_data.get('email')
            # send_mail(mail_subject, message, from_email, to_email, fail_silently=True)
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return redirect('login')
    
    else:
        form = forms.RegistrationForm()
    return render(request, 'Users/register.html', context = {'form' : form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user12 = Alumni_User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user12 = None
    if user12 is not None and account_activation_token.check_token(user12, token):
        user12.is_active = True
        user12.save()
        #login(request, user)
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        return redirect('login')
    else:
        return HttpResponse('Activation link is invalid!')

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


def forget_password(request):
    #print('hello')
    if request.method == 'POST':
        email = request.POST['email']
        user12=None
        #print('hello')
        #print(email)
        try :
            user12 = Permanent_User.objects.get(email=email)
            current_site = get_current_site(request)
            message = render_to_string('Users/reset/password_reset_email.html', {
                'user':user12, 'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user12.pk)),
                'token': account_activation_token.make_token(user12),
            })
            mail_subject = 'Password Reset'
            email = EmailMessage(mail_subject, message, to=[email])
            email.send()
            return redirect('login')
        except(TypeError, ValueError,User.DoesNotExist):
            return HttpResponse('Email is not registered!!')
    form = forms.ForgetForm()
    return render(request, 'Users/reset/reset_form.html',context={'form':form})

def password_reset_confirm(requests,uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user12 = Permanent_User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user12 = None
    if user12 is not None and account_activation_token.check_token(user12, token):
        form = forms.PasswordUpdationForm()
        context={
            'form':form,
            'user12':user12 
        }
        return render(requests, 'Users/reset/password_updation.html',context)
    

    else:
        return HttpResponse('Activation link is invalid!')

def password_updation(requests):
    if requests.method == 'POST':
        form = forms.PasswordUpdationForm(requests.POST)
        #print(form.password)
        if form.is_valid():
            email = requests.POST['email']
            password = requests.POST['password']
            password=make_password(password)
            user34 = Permanent_User.objects.filter(email=email).update(password=password)
            return redirect('login')
        
        


    

    

