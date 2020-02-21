from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.SimplePost, name='home'),
    path('about/', views.SimplePost, name='about'),
]
