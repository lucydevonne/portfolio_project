# skills/views.py
from django.shortcuts import render
from .models import Skill

def skills_view(request):
    skills = Skill.objects.all()
    return render(request, 'skills/skills.html', {'skills': skills})
