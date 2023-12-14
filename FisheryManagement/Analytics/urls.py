from django.urls import path
from . import views

app_name = "Analytics"

urlpatterns = [
    path('forms/', views.isforms, name="forms"),
    path('OverallCatchdash/', views.loadingdash, name="OverallCatchdash"),
    path('unloadingDashData/', views.dataUnloadingDash, name="dataUnloadingDash"),
    path('FishCatchdash/', views.unloadingdash, name="FishCatchdash"),
    path('admindashboard/', views.isadmindashboard, name="admindashboard"),
    path('userstable/', views.userstable, name="userstable"),
    path('loadHistory/', views.loadhistory, name="loadhistory"),
    path('unloadHistory/', views.unloadhistory, name="unloadhistory"),
    path('edituser/<int:id>/', views.edit_user, name="edituser"),
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'),
]