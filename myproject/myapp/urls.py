from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Головна сторінка
    path('contact/', views.contact, name='contact'),  # Сторінка контактів
]
