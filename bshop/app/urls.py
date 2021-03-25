"""bshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import (
    include,
    path,
    re_path,
)

from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url, include
from app.views import views

from django.contrib import admin

schema_view = get_swagger_view(title='API')

router = DefaultRouter()
router.register(r'service', views.ServicesViewSet)
router.register(r'professional', views.ProfessionalsViewSet)
router.register(r'establishment', views.EstablishmentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get_token', obtain_auth_token, name='obtain_token'),
    path('docs/', schema_view, name='docs'),
]
