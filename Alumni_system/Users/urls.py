from django.urls import path
from . import views


urlpatterns = [
    path('', views.on_bording, name = 'home'),
    path('user-home/', views.home, name = 'user-homepage'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login')
]