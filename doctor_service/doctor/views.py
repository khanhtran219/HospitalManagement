# trong file views.py
from rest_framework import viewsets
from .models import Doctor, WorkSchedule
from .serializers import DoctorSerializer, WorkScheduleSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class WorkScheduleViewSet(viewsets.ModelViewSet):
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleSerializer
