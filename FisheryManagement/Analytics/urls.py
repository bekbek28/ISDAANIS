from django.urls import path
from . import views


urlpatterns = [
    path('homepage/', views.index),
    path('forms/', views.isforms),
    path('dashboard/', views.isdashboard),
    ]