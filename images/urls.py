from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('home', views.home, name='home'),

    path('viewPhoto/<str:pk>/', views.viewPhoto, name='viewPhoto'),
    path('addPhoto/', views.addPhoto, name='addPhoto'),
    path('search_category/', views.search_category, name='search_category'),
    path('search_location/', views.search_location, name='search_location'),
]