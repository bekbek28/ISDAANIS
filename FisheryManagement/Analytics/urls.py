from django.urls import path
from . import views

app_name = "Analytics"

urlpatterns = [
    path('forms/', views.isforms, name="forms"),
    path('loadingdash/', views.loadingdash, name="loadingdash"),
    path('unloadingdash/', views.unloadingdash, name="unloadingdash"),
    path('admindashboard/', views.isadmindashboard, name= "admindashboard"),
    path('userstable/', views.userstable, name= "userstable"),
    path('analyticsTable/', views.analyticsTable, name= "analyticsTable"),
    path('loadHistory/', views.loadhistory, name= "loadhistory"),
    path('unloadHistory/', views.unloadhistory, name= "unloadhistory"),
    path('editUser/', views.edit_user, name= "edituser"),
    path('logout/', views.logout_view, name='logout'),
]