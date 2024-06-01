from django.db import models

class Appointment(models.Model):
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    appointment_date = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ])

    def __str__(self):
        return f'Appointment {self.id} - Patient {self.patient_id} with Doctor {self.doctor_id}'
