from django.urls import path
from . import views

app_name = "Authentication"

urlpatterns = [
    path('homepage/', views.index),
    path('' , views.usertype, name='usertype'),
    path('login/' , views.islogin, name='login'),
    path('register/' , views.isreghtml, name='register'),
    path('pmlogin/' , views.ispmloginhtml, name='pmlogin'),
    path('pmreg/' , views.ispmreghtml, name='pmregister'),
    path('loginadmin/' , views.ispmloginhtml, name='loginadmin'),
    path('regadmin/' , views.isadminreghtml, name='registeradmin'),
]