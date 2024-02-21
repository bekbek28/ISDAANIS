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
    path('analytics/delete/<int:id>/', views.delete_unload_history, name='delete_unload_history'),
    path('edit-recentlist/<int:id>/', views.edit_recentlist, name='edit_recentlist'),
    path('delete-recentlist/<int:id>/', views.delete_recentlist, name='delete_recentlist'),

]
