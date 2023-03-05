from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name="home"),
    path('responsivas/', views.responsivas, name="responsivas"),
]