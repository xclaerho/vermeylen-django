from django.urls import path
from . import views

app_name = 'augustjes'
urlpatterns = [
    path('', views.AugustjeListView.as_view(), name='list'),
    path('<int:pk>/', views.AugustjeDetailView.as_view(), name='detail'),
]