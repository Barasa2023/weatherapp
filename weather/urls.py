from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('', views.index, name='index'),
    #path('forecast/', views.forecast, name='forecast'),
    #path('about/', views.about, name='about'),
]