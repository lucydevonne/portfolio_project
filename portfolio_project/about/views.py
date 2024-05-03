# about/views.py
from django.shortcuts import render
from .models import About

def about_view(request):
    about_info = About.objects.first()  # Assuming there's only one About object
    return render(request, 'about/about.html', {'about_info': about_info})
