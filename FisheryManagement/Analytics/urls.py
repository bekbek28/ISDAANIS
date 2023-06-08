from django.urls import path
from . import views

app_name = "Analytics"

urlpatterns = [
    path('homepage/', views.index),
    path('forms/', views.isforms, name="forms"),
    path('dashboard/', views.isdashboard, name="dashboard"),
    path('admindashboard/', views.isadmindashboard, name= "admindashboard"),
    ]