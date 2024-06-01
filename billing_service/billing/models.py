from django.db import models

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=50, unique=True)
    patient_id = models.IntegerField()  # Assume patient ID is an integer
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_issued = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
    ])

    def __str__(self):
        return f'Invoice {self.invoice_number} - {self.amount}'

class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='payments', on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=[
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
    ])

    def __str__(self):
        return f'Payment for {self.invoice.invoice_number} - {self.amount_paid}'
