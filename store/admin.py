from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price','image', 'category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'password', 'email', 'phone' ]

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)