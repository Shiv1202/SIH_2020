from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.on_bording, name = 'home'),
    path('user-home/', views.home, name = 'user-homepage'),
    path('register/', views.register, name = 'register'),
   url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('login/', views.login, name = 'login')
]