from django.urls import path
from . import views

urlpatterns = [
    path("", views.products, name='products-list'),
    path("add", views.addProduct, name='add-product'),
    path("edit/<str:id>", views.editProduct, name='edit-product'),
    path("orders", views.Orders, name='orders-list'),
    path("create", views.createOrder, name='create-order'),
    path("update/<str:id>", views.updateOrder, name='update-order'),
    path("detail/<str:id>", views.orderDetail, name='order-detail'),
    path("detail/<str:id>/deliver", views.deliverOrder, name='deliver-order'),
]