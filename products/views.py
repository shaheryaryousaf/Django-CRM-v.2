from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, Order, Category
from .forms import ProductForm, OrderForm, CategoryForm


# ===============================
# Categories List
# ===============================
def categories(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories-list')
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'form': form
    }
    return render(request, 'products/categories/categories.html', context)


# ===============================
# Delete Category
# ===============================
def deleteCategory(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('categories-list')


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
# Delete Product
# ===============================
def deleteProduct(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


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


# ===============================
# Delete Order
# ===============================
def deleteOrder(request, id):
    order = Order.objects.get(id=id)
    order.delete()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))