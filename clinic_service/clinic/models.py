from django.db import models

class ClinicRoom(models.Model):
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f'Room {self.room_number} ({self.room_type}) - {self.department}'

class Bed(models.Model):
    room = models.ForeignKey(ClinicRoom, related_name='beds', on_delete=models.CASCADE)
    bed_number = models.CharField(max_length=10)
    status = models.CharField(max_length=20, choices=[
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('maintenance', 'Maintenance'),
    ])

    def __str__(self):
        return f'Bed {self.bed_number} in Room {self.room.room_number}'
