from django.forms import ModelForm
from .models import Product, Order


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at',)


class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ('created_at',)


class CustomerOrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ('created_at','customer')