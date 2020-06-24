from django.urls import path
from .views import covid
from covid import views


urlpatterns = [
    path('',views.covid,name='covid'),
    path('covid/',views.covid, name='covid'),
    path('covid_2/',views.covid_2,name='covid_2')
]