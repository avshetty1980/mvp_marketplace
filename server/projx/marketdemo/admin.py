from django.contrib import admin
import django.apps
from .models import Product, Location, Land, Seller, Buyer, Delivery, Escrow
# from . import models

# Register your models here.

# admin.site.register(Product)
# admin.site.register(Location)
# admin.site.register(Land)
# admin.site.register(Seller)

# models = django.apps.apps.get_models()

# for model in models:
#     try:
#         admin.site.register(model)

#     except admin.sites.AlreadyRegistered:
#         pass


# admin.site.unregister(django.contrib.sessions.models.Session)

# class ProductAdmin(admin.ModelAdmin):
#     fields = ['unit_price', 'category', 'name', 'variety', 'avail_weight', 'quantity']


# admin.site.register(Product, ProductAdmin)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'variety',
                    'in_stock', 'avail_weight', 'unit_price']
    list_filter = ['in_stock', 'unit_price']
    list_editable = ['in_stock', 'unit_price']


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['is_active']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['area', 'city']


# @admin.register(Buyer)
# class BuyerAdmin(admin.ModelAdmin):
#     list_display = ['']


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'status']
    list_filter = ['price_km', 'price_kg']


@admin.register(Escrow)
class EscrowAdmin(admin.ModelAdmin):
    list_display = ['status']
