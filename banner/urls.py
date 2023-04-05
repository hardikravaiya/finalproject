from django.contrib import admin
from django.urls import path
from django.urls import path,include
from banner import views

urlpatterns = [
     path('',views.index),
     path('contact/', views.con),
     path('about/', views.about),
     path('notes/', views.notes),
     path('profile/',views.Profile),
     path('userlogout/',views.userlogout),
]




