from django.urls import path
from . import views

urlpatterns = [
    path('evaluate/', views.turn_to_evaluate),
    path('evaluate/submit/', views.submit),
    path('evaluate/first/', views.turn_to_first),
    path('evaluate/last/', views.turn_to_last),
    path('evaluate/pre/', views.turn_to_pre),
    path('evaluate/next/', views.turn_to_next)
]