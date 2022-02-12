from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='shopIndex'),
    path('addToCart/', views.addToCart, name='addToCart')
]