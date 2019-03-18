from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.info, name='info'),
    path('clublied/', views.clublied, name='clublied'),
    path('archief/', views.archief, name='archief'),
    path('praesidium/', views.praesidium, name='praesidium')
]