from django.urls import path
from . import views
from .views import logout_view

app_name = "Analytics"

urlpatterns = [
    path('forms/', views.isforms, name="forms"),
    path('dashboard/', views.isdashboard, name="dashboard"),
    path('admindashboard/', views.isadmindashboard, name= "admindashboard"),
    path('logout/', logout_view, name='logout'),
    ]