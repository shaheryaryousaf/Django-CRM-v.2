from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomerForm
from products.forms import SearchForm
from products.forms import CustomerOrderForm
from .models import Customer
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# ===============================
# Customers List
# ===============================
@login_required(login_url='/account/signin')
def customers(request):
    customers = Customer.objects.all()

    paginator = Paginator(customers,5)
    page_number = request.GET.get('page')
    if page_number and int(page_number) < 1:  # Check if page number is less than 1
        page_number = 1
    page_obj = paginator.get_page(page_number)

    context = {
        'customers': customers,
        'page_obj': page_obj,
    }
    return render(request, 'customers/customers.html', context)


# ===============================
# Add Customer
# ===============================
@login_required(login_url='/account/signin')
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
@login_required(login_url='/account/signin')
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
@login_required(login_url='/account/signin')
def customerDetail(request, id):
    customer = Customer.objects.get(id=id)
    orders = customer.order_set.all()

    form = SearchForm(request.GET)

    if form.is_valid():
        if form.cleaned_data['product']:
            orders = orders.filter(product=form.cleaned_data['product'])
        if form.cleaned_data['status']:
            orders = orders.filter(status=form.cleaned_data['status'])

    paginator = Paginator(orders,5)
    page_number = request.GET.get('page')
    if page_number and int(page_number) < 1:  # Check if page number is less than 1
        page_number = 1
    page_obj = paginator.get_page(page_number)

    context = {
        'customer': customer,
        'orders': orders,
        'form': form,
        'page_obj': page_obj
    }
    return render(request, 'customers/customer-detail.html', context)


# ===============================
# Add Customer Order
# ===============================
@login_required(login_url='/account/signin')
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