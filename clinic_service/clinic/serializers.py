from rest_framework import serializers
from .models import ClinicRoom, Bed

class ClinicRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicRoom
        fields = '__all__'

class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bed
        fields = '__all__'
