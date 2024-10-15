from django.shortcuts import render

# Представлення для головної сторінки
def home_view(request):
    return render(request, 'home.html')

# Представлення для сторінки контактів
def contact(request):
    return render(request, 'contact.html')
