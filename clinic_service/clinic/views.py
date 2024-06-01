from rest_framework import viewsets
from .models import ClinicRoom, Bed
from .serializers import ClinicRoomSerializer, BedSerializer

class ClinicRoomViewSet(viewsets.ModelViewSet):
    queryset = ClinicRoom.objects.all()
    serializer_class = ClinicRoomSerializer

class BedViewSet(viewsets.ModelViewSet):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
