from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from staff.views import StaffViewSet

router = DefaultRouter()
router.register(r'staff', StaffViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
