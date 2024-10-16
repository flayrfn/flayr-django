from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')







