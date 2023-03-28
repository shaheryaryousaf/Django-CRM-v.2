from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, Order, Category
from .forms import ProductForm, OrderForm, CategoryForm, SearchForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# ===============================
# Categories List
# ===============================
@login_required(login_url='/account/signin')
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
@login_required(login_url='/account/signin')
def products(request):
    products = Product.objects.all()

    paginator = Paginator(products,5)
    page_number = request.GET.get('page')
    if page_number and int(page_number) < 1:  # Check if page number is less than 1
        page_number = 1
    page_obj = paginator.get_page(page_number)

    context = {
        'products': products,
        'page_obj': page_obj
    }
    return render(request, 'products/products.html', context)


# ===============================
# Add Product
# ===============================
@login_required(login_url='/account/signin')
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
@login_required(login_url='/account/signin')
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
@login_required(login_url='/account/signin')
def deleteProduct(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


# ===============================
# Orders List
# ===============================
@login_required(login_url='/account/signin')
def Orders(request):
    orders = Order.objects.all()
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
        'orders': orders,
        'page_obj': page_obj,
        'form': form
    }
    return render(request, 'products/orders.html', context)


# ===============================
# Order Detail
# ===============================
@login_required(login_url='/account/signin')
def orderDetail(request, id):
    order = Order.objects.get(id=id)
    context = {
        'order': order
    }
    return render(request, 'products/order-detail.html', context)


# ===============================
# Create Order
# ===============================
@login_required(login_url='/account/signin')
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
@login_required(login_url='/account/signin')
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
@login_required(login_url='/account/signin')
def deliverOrder(request, id):
    order = Order.objects.get(id=id)
    order.status='Delivered'
    order.save()
    return redirect('orders-list')


# ===============================
# Delete Order
# ===============================
@login_required(login_url='/account/signin')
def deleteOrder(request, id):
    order = Order.objects.get(id=id)
    order.delete()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))