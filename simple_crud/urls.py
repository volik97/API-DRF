"""simple_crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from measurements.views import ProjectViewSet, MeasurementViewSet
from rest_framework.routers import SimpleRouter

# TODO: настройте роутер и подключите `ProjectViewSet` и `MeasurementViewSet`

router = SimpleRouter()
router.register('api/v1/project', ProjectViewSet, basename='project')
router.register('api/v1/measure', MeasurementViewSet, basename='measure')

urlpatterns = [
    path('admin/', admin.site.urls),
] + router.urls
