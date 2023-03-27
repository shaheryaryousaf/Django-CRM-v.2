from django.contrib import admin
from .models import Category, Product, Order


# ===============================
# Category Admin Table Display
# ===============================
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    list_per_page = 15


# ===============================
# Product Admin Table Display
# ===============================
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    list_display_links = ('id', 'title')
    list_per_page = 15


# ===============================
# Order Admin Table Display
# ===============================
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'status')
    list_display_links = ('id',)
    list_editable = ('status',)
    list_per_page = 15


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)