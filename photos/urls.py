from django.urls import path
from . import views

app_name = 'photos'
urlpatterns = [
    path('', views.GalleryListView.as_view(), name='list'),
    path('<int:pk>/', views.GalleryDetailView.as_view(), name='detail'),
]