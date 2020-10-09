from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from django.contrib.auth.hashers import make_password,check_password


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


def validateCustomer(customer):
    error = None
    if (not customer.first_name):
        error = "First Name Required !!"
    elif len(customer.first_name) < 4:
        error = 'First Name must be 4 char long or more'
    elif not customer.last_name:
        error = 'Last Name Required'
    elif len(customer.last_name) < 4:
        error = 'Last Name must be 4 char long or more'
    elif not customer.phone:
        error = 'Phone Number required'
    elif len(customer.phone) < 10:
        error = 'Phone Number must be 10 char Long'
    elif len(customer.password) < 6:
        error = 'Password must be 6 char long'
    elif len(customer.email) < 5:
        error = 'Email must be 5 char long'
    elif customer.isExist():
        error = 'Email Address Already Registered'
    return error

def registerUser(request):
    pp = request.POST
    first_name = pp.get('firstname')
    last_name = pp.get('lastname')
    phone = pp.get('phone')
    email = pp.get('email')
    password = pp.get('password')
    value = {
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone,
        'email': email
    }
    customer = Customer(
        first_name=first_name,
        last_name=last_name,
        phone=phone,
        email=email,
        password=password,
    )
    error = validateCustomer(customer)

    if not error:
        customer.password = make_password(customer.password)
        customer.register()
        return redirect('homepage')

    else:
        data = {
            'error': error,
            'values': value
        }
        return render(request, 'signup.html', data)

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        return  registerUser(request)

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error = None
        if customer:
           ok= check_password(password, customer.password)
           if ok:
               return redirect('homepage')
           else:
               error = 'Password invalid !'
        else:
            error = 'Email or Password invalid !'
        return render(request,'login.html',{'error':error})







