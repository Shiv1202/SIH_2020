from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    # path('', views.on_bording, name = 'index'),
    # path('user-register/', views.register, name = 'user-register'),
    # path('user-login/', views.login, name = 'user-login'), 
    # path('dashboard-user/', views.user_dashboard, name = 'dashboard-user'),
    # url(r'$', views.on_bording, name = 'home'),
    # url(r'^user-register/$', views.register, name = 'user-register'),
    # url(r'^user-login/$', views.login, name = 'user-login'),
    # url(r'^user-home/$', views.home, name = 'user-homepage')
    path('', views.on_bording, name = 'home'),
    path('user-home/', views.home, name = 'user-homepage'),
    path('register/', views.register, name = 'register'),
   url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('login/', views.login, name = 'login'),
    path('forget-password/',views.forget_password,name='forget-password'),
    path(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
          views.password_reset_confirm,name='password-link'),
    path('password-updation/',views.password_updation,name='password-updation')

]