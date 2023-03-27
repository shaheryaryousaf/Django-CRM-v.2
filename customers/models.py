from datetime import datetime
from django.db import models

STATUS = (
    ('Assigned', 'Assigned'),
    ('Unassigned', 'Unassigned'),
)

# Customers Model
class Customer(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(
        null=True, blank=True, default=datetime.now)

    def __str__(self):
        return self.first_name

    def get_date(self):
        return self.created_at.date()

    class Meta:
        verbose_name_plural = "Customers"