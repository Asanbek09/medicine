from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.clientsList, name='all'),
    path('create/', views.createClient, name='create')
]
