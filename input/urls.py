from django.urls import path
from . import views

app_name = 'input'
urlpatterns = [
    path('', views.index, name='input'),
]