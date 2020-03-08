from django.conf.urls import url
from django.urls import path, include

from . import views



urlpatterns = [
    path('', views.SimplePost),
    path('lab/', views.LabPost),
    path('lab/<str:toolu>/', views.LabPost),
    path('<str:lmenu>/', views.SimplePost),
    path('<str:lmenu>/<str:postname>/', views.SimplePost),
    #path('', views.SimplePost, name='about'),
]
