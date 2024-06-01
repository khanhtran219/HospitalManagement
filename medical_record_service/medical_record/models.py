from django.db import models


class MedicalRecord(models.Model):
    patient_id = models.CharField()
    # Thêm các trường khác cho hồ sơ y tế
    medical_history = models.TextField()
    test_results = models.TextField()
    prescriptions = models.TextField()

    def __str__(self):
        return f'Medical Record for {self.patient.first_name} {self.patient.last_name}'
