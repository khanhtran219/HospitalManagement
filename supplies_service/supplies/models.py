from django.db import models

class Pharmaceutical(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=100)
    expiration_date = models.DateField()

    def __str__(self):
        return f'{self.name} ({self.type})'

class MedicalSupply(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.type})'
