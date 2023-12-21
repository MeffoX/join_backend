"""
URL configuration for joinbackend project.

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
from django.contrib import admin
from django.urls import path

from join_backend.views import add_contact, get_contacts, get_users, login_view, register_user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signup/', register_user_view, name='api_signup'),
    path('api/login/', login_view, name='api_login'),
    path('api/users/', get_users, name='api_users'),
    path('api/add_contact/', add_contact, name='add_contact'),
    path('api/contacts/', get_contacts, name='get_contacts'),
]
