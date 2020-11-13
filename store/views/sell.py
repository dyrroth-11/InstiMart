from django.shortcuts import render, redirect
from store.models.customer import Customer
from store.models.category import Category
from store.models.product import Product
from django.views import View


class Sell(View):
    def get(self, request):
        return render(request, 'sell.html')

    def post(self, request):
        print('kya ho gya ye')
        return Sell.addProduct(self, request)

    def addProduct(self, request):
        pp = request.POST
        print(request)
        product_name = pp.get('productname')
        price = pp.get('price')
        des = pp.get('des')
        image = pp.get('image')
        gp = Category(
            name="Furniture",
        )
        gp.save();
        value = {
            'name': product_name,
            'price': price,
            'category': gp,
            'description': des,
            'image': image
        }
        product = Product(
            name=product_name,
            price=price,
            category=gp,
            description=des,
            image=request.FILES.get('image'),
        )
        print(product_name)
        print(price)
        print(des)
        print(gp)
        print(image)
        error = self.validateProduct(product)
        data = {
            'error': error,
            'values': value
        }
        return render(request, 'thanks.html', data)

    def validateProduct(self, customer):
        error = None
        if (not customer.name):
            error = "Product Name Required !!"
        elif not customer.price:
            error = 'Price Required'
        elif not customer.description:
            error = 'Description required'
        elif not customer.image:
            error = 'Image required'
        elif not customer.category:
            error = 'category required'

        return error
