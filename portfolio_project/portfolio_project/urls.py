"""
URL configuration for portfolio_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# portfolio_project/urls.py
from django.contrib import admin
from django.urls import path, include
from about.views import about_view
from projects.views import projects_view
from skills.views import skills_view
from contact.views import contact_view
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about_view, name='about'),
    path('projects/', projects_view, name='projects'),
    path('skills/', skills_view, name='skills'),
    path('contact/', contact_view, name='contact'),
    path('contact/success/', TemplateView.as_view(template_name='contact/contact_success.html'), name='contact_success'),
]
