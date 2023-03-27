from django.urls import path
from . import views

urlpatterns = [
    path("", views.customers, name='customers-list'),
    path("add", views.addCustomer, name='add-customer'),
    path("edit/<str:id>", views.updateCustomer, name='update-customer'),
    path("detail/<str:id>", views.customerDetail, name='customer-detail'),
    path("detail/<str:id>/order", views.addCustomerOrder, name='add-customer-order'),
]