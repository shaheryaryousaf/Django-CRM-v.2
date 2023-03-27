from datetime import datetime
from django.db import models
from customers.models import Customer

STATUS = (
    ('Pending', 'Pending'),
    ('Out for Delivery', 'Out for Delivery'),
    ('Delivered', 'Delivered'),
)


# Ctageory Model
class Category(models.Model):
    title = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


# Products Model
class Product(models.Model):
    title = models.CharField(max_length=255, null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(
        null=True, blank=True, default=datetime.now)

    def __str__(self):
        return self.title

    def get_date(self):
        return self.created_at.date()

    class Meta:
        verbose_name_plural = "Products"


# Orders Model
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=20, choices=STATUS, default='Unassigned', null=True)
    created_at = models.DateTimeField(
        null=True, blank=True, default=datetime.now)

    def __str__(self):
        return self.customer.first_name

    def get_date(self):
        return self.created_at.date()

    class Meta:
        verbose_name_plural = "Orders"