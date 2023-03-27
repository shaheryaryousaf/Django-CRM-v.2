from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomerForm
from products.forms import CustomerOrderForm
from .models import Customer

# ===============================
# Customers List
# ===============================
def customers(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }
    return render(request, 'customers/customers.html', context)


# ===============================
# Add Customer
# ===============================
def addCustomer(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"New customer has been added.")
            return redirect('customers-list')
    context = {
        'form': form
    }
    return render(request, 'customers/add-customer.html', context)


# ===============================
# Update Customer
# ===============================
def updateCustomer(request, id):
    customer = Customer.objects.get(id=id)
    form = CustomerForm(instance=customer)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, f"Customer has been update.")
            return redirect('customers-list')
    context = {
        'form': form
    }
    return render(request, 'customers/update-customer.html', context)


# ===============================
# Customer Detail
# ===============================
def customerDetail(request, id):
    customer = Customer.objects.get(id=id)
    context = {
        'customer': customer
    }
    return render(request, 'customers/customer-detail.html', context)


# ===============================
# Add Customer Order
# ===============================
def addCustomerOrder(request, id):
    customer = Customer.objects.get(id=id)
    form = CustomerOrderForm()
    if request.method == "POST":
        form = CustomerOrderForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.customer=customer
            f.save()
            messages.success(request, f"New order has been created for {customer.first_name} {customer.last_name}.")
            return redirect('customer-detail', customer.id)
    context = {
        'form': form,
        'customer': customer
    }
    return render(request, 'customers/create-customer-order.html', context)