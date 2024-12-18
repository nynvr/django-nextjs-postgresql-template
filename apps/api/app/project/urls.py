"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('project/', include('project.urls'))
"""
from django.contrib import admin
from django.urls import include, re_path
from rest_framework import routers

# Wire up our API using automatic URL routing.
router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    re_path('api/', include(router.urls)),
    re_path('api/auth/', include('rest_framework.urls')),
    re_path('admin/', admin.site.urls),
]