from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.orders import Orders
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View


class CheckOut(View):
    def post(self, request):
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_product_by_id(list(cart.keys()))

        for product in products:
            order = Orders(
                customer = Customer(id = customer),
                product = product,
                price = product.price,
                address = address,
                phone = phone,
                quantity=cart.get(str(product.id))
            )
            order.placeOrder()
            request.session['cart']={}
        return redirect('cart')




