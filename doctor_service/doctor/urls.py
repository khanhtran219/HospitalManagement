# trong file urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, WorkScheduleViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'work-schedules', WorkScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
