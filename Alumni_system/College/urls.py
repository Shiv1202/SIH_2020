from django.urls import path
from . import views
from django.conf.urls import url




urlpatterns = [

    #path('', views.on_bording, name = 'index'),
    path('college-home/', views.college_home, name = 'college-home')
    # url(r'^college-home/$', views.college_home, name = 'college-home')
    # path('college-login/', views.college_login, name = 'college_login')
    
]