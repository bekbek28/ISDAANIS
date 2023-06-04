from django.urls import path
from . import views


urlpatterns = [
    path('homepage/', views.index),
    path('login/' , views.login, name='login'),
    path('register/' , views.isreghtml, name='register'),
    path('pmlogin/' , views.ispmloginhtml, name='pmlogin'),
    path('pmreg/' , views.ispmreghtml, name='pmregister'),
]