from django.urls import path
from .views import home
from article import views
from .views import LoginView


urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('clear', views.clear_articles, name='clear_articles'),

]

