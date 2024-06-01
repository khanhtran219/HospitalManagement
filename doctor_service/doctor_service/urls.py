from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from doctor.urls import urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urlpatterns)),
]
