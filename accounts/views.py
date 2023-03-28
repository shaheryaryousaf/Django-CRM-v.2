from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from customers.models import Customer
from products.models import Order

# ===============================
# Dashboard
# ===============================
@login_required(login_url='/account/signin')
def dashboard(request):
    customers = Customer.objects.all()[:5]
    orders = Order.objects.all()[:5]
    context = {
        'customers': customers,
        'orders': orders,
        'customers_count': Customer.objects.all().count(),
        'orders_count': Order.objects.all().count(),
        'delivered_orders': Order.objects.filter(status='Delivered').count(),
        'pending_orders': Order.objects.filter(status='Pending').count(),
    }
    return render(request, 'accounts/dashboard.html', context)