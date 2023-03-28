from django.forms import ModelForm
from .models import Product, Order, Category
from django import forms


STATUS = (
    ('Pending', 'Pending'),
    ('Out for Delivery', 'Out for Delivery'),
    ('Delivered', 'Delivered'),
)


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('title',)


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


class SearchForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), required=False)
    status = forms.ChoiceField(choices=STATUS, required=False)