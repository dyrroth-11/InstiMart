from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.order import Order
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View


class OrderView(View):
    def get(self,request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        return render(request,'orders.html',{'orders':orders})




