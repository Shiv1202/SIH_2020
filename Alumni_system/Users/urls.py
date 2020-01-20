from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.on_bording, name = 'index'),
    path('user-register/', views.register, name = 'user-register'),
    path('user-login/', views.login, name = 'user-login'), 
    path('dashboard-user/', views.user_dashboard, name = 'dashboard-user'),
    # url(r'$', views.on_bording, name = 'home'),
    # url(r'^user-register/$', views.register, name = 'user-register'),
    # url(r'^user-login/$', views.login, name = 'user-login'),
    # url(r'^user-home/$', views.home, name = 'user-homepage')
]