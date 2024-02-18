from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "Authentication"

urlpatterns = [
    path('PortManager', views.isLandingPage, name='landingPage'),
    path('MarketChecker', views.isMCLandingPage, name='MClandingPage'),
    path('login/', views.islogin, name='login'),
    path('register/', views.isreghtml, name='register'),
    path('pmlogin/', views.ispmloginhtml, name='pmlogin'),
    path('pmreg/', views.ispmreghtml, name='pmregister'),
    path('loginadmin/', views.isadminloginhtml, name='loginadmin'),
    path('regadmin/', views.isadminreghtml, name='registeradmin'),


    # Password Reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
