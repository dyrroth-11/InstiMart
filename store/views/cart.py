from django.shortcuts import render, redirect
from store.models.product import Product
from django.contrib.auth.hashers import check_password
from django.views import View


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart',{}).keys())
        x = bool(ids)
        print(ids)
        if not x:
            print("a")
            products
            return render(request, 'cart.html',)
        else:
            print("b")
            products = Product.get_product_by_id(ids)
            print(products)
            return render(request, 'cart.html', {'products': products})




