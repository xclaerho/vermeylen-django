from django.urls import path

from . import views

app_name = 'muilgraaf'
urlpatterns = [
    path('', views.muilgraaf, name='muilgraaf'),
]