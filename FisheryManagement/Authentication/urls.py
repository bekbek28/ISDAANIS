from django.urls import path
from . import views


urlpatterns = [
    path('homepage/', views.index),
    path('login' , views.ishtml, name='mclogin'),
    path('Register' , views.isreghtml, name='mcregister'),
    path('pmlogin' , views.ispmloginhtml, name='pmlogin'),
    path('pmreg' , views.ispmreghtml, name='pmreg '),
]