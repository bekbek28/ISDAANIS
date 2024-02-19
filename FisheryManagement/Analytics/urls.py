from django.urls import path
from . import views

app_name = "Analytics"

urlpatterns = [
    path('forms/', views.isforms, name="forms"),
    path('RecentList/', views.recentList, name="recentlist"),
    path('OverallCatchdash/', views.OCdash, name="OverallCatchdash"),
    path('unloadingDashData/', views.dataUnloadingDash, name="dataUnloadingDash"),
    path('FishCatchdash/', views.FCdash, name="FishCatchdash"),
    path('admindashboard/', views.isadmindashboard, name="admindashboard"),
    path('userstable/', views.userstable, name="userstable"),
    path('unloadHistory/', views.unloadhistory, name="unloadhistory"),
    path('edituser/<int:id>/', views.edit_user, name="edituser"),
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'),
    path('edit/<int:id>/', views.edit_unloading, name='edit_unloading'),
    path('delete-transaction/<int:id>/', views.delete_transaction, name='delete_transaction'),
    path('edit/recent/<int:id>/', views.edit_recent_transaction, name='edit_recent_transaction'),
    path('delete/<int:id>/', views.delete_recent, name='delete_recent')


]