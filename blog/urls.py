from django.urls import path
from . import views

urlpatterns = [
    path('', views.bloglist, name='blog'),
    path('imitation-learning/', views.imitationlearning, name='imitationlearning'),
]