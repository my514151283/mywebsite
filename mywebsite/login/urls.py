from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.turn_to_login),
    path('login/login/', views.login),
    path('login/logout/', views.logout),
    path('login/register/', views.turn_to_register),
    path('login/register/register/', views.register),
]