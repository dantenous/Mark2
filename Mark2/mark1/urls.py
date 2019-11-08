from django.urls import path, include
from . import views
from .views import ChartData  # Naimportuje tridu ChartData, aby se dala pouzit
from .views import SerialView  # Naimportuje tridu Serial, aby se dala pouzit

urlpatterns = [
    # Zobrazovaci stranka po overeni Usera
    path('index', views.index, name='index'),
    path('', views.uvod, name='uvod'),  # Uvodni stranka pro prihlaseni
    # REST api pro zobrazovani dat
    path('api/chart/data/', ChartData.as_view()),
    # REST api pro zobrazovani dat
    path('api/serial/data/', SerialView.as_view()),
    path('logout', views.logout, name='logout'),  # Odhlaseni
]
