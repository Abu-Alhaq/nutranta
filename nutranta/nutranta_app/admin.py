from django.contrib import admin
from .models import Customer, Product, Cart, OrderPlaced , Address , Contact

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode', 'state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'description', 'category', 'product_image','total_calroes','total_fat','total_protein','total_carbohydrates','total_sodium','total_sugar','total_cholesterol','total_potassium','total_calcium','total_vitamin_d','total_fiber']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'product', 'quantity', 'ordered_date', 'status']

@admin.register(Address)
class AddressModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'address', 'zipcode', 'state']


@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'message']

