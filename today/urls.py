from django.urls import path
from . import views

urlpatterns = [
    path('today/', views.index, name='today'),
    path('today/summary', views.show, name='summary'),
]
