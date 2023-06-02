from django.urls import path
from . import views


urlpatterns = [
    path('homepage/', views.index),
    path('login' , views.ishtml, name='login'),
    path('Register' , views.isreghtml, name='register'),
]