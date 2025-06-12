from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('about/', views.index, name='about'),
    path('contact/', views.index, name='contact'),
    path('shop-single/', views.index, name='shop')
]