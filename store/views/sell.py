from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View


class Sell(View):
    def get(self, request):
        return render(request, 'sell.html')

    def post(self, request):
        return registerUser(request)

    def registerUser(self, request):
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
        error = self.validateCustomer(customer)

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

    def validateCustomer(self, customer):
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
