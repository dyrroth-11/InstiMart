from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
# Create your views here.

def index(request):
    products = Product.get_all_products()
    categories = Category.get_all_categories()
    data = {}
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()

    data['products'] = products
    data['categories'] = categories
    return render(request,'index.html' ,data)


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        pp = request.POST
        first_name = pp.get('firstname')
        last_name = pp.get('lastname')
        phone = pp.get('phone')
        email = pp.get('email')
        password = pp.get('password')
        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            password=password,
        )
        customer.register()

        return HttpResponse('Signup successful')
