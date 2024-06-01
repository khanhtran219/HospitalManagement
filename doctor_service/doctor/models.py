from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField(max_length=200)
    gender = models.IntegerField()
    role = models.CharField(max_length=50)
    days = models.CharField(max_length=50)
    display_schedule = models.CharField(max_length=100)
    subject_id = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.CharField(max_length=50)
    room = models.CharField(max_length=100, null=True, blank=True)
    booking_note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class WorkSchedule(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='work_schedule', on_delete=models.CASCADE)
    date = models.DateField()
    time_slots = models.JSONField()

    def __str__(self):
        return f"{self.doctor.name} - {self.date}"