from django.urls import path, include , re_path
from django.urls import re_path as url
from . import views
from django.urls import path, include

app_name = 'login' 
urlpatterns = [
    url('', views.user_login, name='user_login'),
   
    
   
]