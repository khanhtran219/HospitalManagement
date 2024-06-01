from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from clinic.views import ClinicRoomViewSet, BedViewSet

router = DefaultRouter()
router.register(r'clinic-rooms', ClinicRoomViewSet)
router.register(r'beds', BedViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
