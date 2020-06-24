from django.contrib import admin
from django.urls import path
from chart import views
from .views import *
from covid.views import covid

urlpatterns = [
    path('',views.home,name='list'),
    path('titanic/',views.titanic, name='titanic'),
]