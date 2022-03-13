from django.urls import path, include
from . import views
from .views import RegistrationAPI

urlpatterns = [
    path('', views.index, name='shopIndex'),
    path('contact/', views.contact, name='contact'),
    path('addToCart/', views.addToCart, name='addToCart'),
    path('product/<int:id>', views.product, name='productView'),
    path('register/', RegistrationAPI.as_view()),
    path('checkout/', views.checkout),
]