from django.contrib import admin
from .models import Customer


# ===============================
# Customers Admin Table Display
# ===============================
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'email', 'phone', 'address')
    list_display_links = ('id', 'first_name')
    list_per_page = 15


admin.site.register(Customer, CustomerAdmin)