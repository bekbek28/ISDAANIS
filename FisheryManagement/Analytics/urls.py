from django.urls import path
from . import views

app_name = "Analytics"

urlpatterns = [
    path('forms/', views.isforms, name="forms"),
    path('dashboard/', views.isdashboard, name="dashboard"),
    path('admindashboard/', views.isadmindashboard, name= "admindashboard"),
    path('userstable/', views.userstable, name= "userstable"),
    path('analyticsTable/', views.analyticsTable, name= "analyticsTable"),
    path('loadHistory/', views.loadhistory, name= "loadhistory"),
    path('logout/', views.logout_view, name='logout'),
]