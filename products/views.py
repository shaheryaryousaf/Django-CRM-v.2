from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, Order
from .forms import ProductForm, OrderForm

# ===============================
# Products List
# ===============================
def products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/products.html', context)


# ===============================
# Add Product
# ===============================
def addProduct(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"New product has been added.")
            return redirect('products-list')
    context = {
        'form': form
    }
    return render(request, 'products/add-product.html', context)


# ===============================
# Update Product
# ===============================
def editProduct(request, id):
    products = Product.objects.get(id=id)
    form = ProductForm(instance=products)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=products)
        if form.is_valid():
            form.save()
            messages.success(request, f"Product has been update.")
            return redirect('products-list')
    context = {
        'form': form
    }
    return render(request, 'products/edit-product.html', context)


# ===============================
# Orders List
# ===============================
def Orders(request):
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'products/orders.html', context)


# ===============================
# Order Detail
# ===============================
def orderDetail(request, id):
    order = Order.objects.get(id=id)
    context = {
        'order': order
    }
    return render(request, 'products/order-detail.html', context)


# ===============================
# Create Order
# ===============================
def createOrder(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"New order has been created.")
            return redirect('orders-list')
    context = {
        'form': form
    }
    return render(request, 'products/create-order.html', context)


# ===============================
# Update Order
# ===============================
def updateOrder(request, id):
    order = Order.objects.get(id=id)
    form = OrderForm(instance=order)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, f"Order has been update.")
            return redirect('orders-list')
    context = {
        'form': form
    }
    return render(request, 'products/update-order.html', context)


# ===============================
# Deliver Order
# ===============================
def deliverOrder(request, id):
    order = Order.objects.get(id=id)
    order.status='Delivered'
    order.save()
    return redirect('orders-list')