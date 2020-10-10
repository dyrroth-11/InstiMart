from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error = None
        if customer:
            ok = check_password(password, customer.password)
            if ok:
                request.session['customer']=customer.id
                return redirect('homepage')
            else:
                error = 'Password invalid !'
        else:
            error = 'Email or Password invalid !'
        return render(request, 'login.html', {'error': error})

def logout(request):
    request.session.clear()
    return redirect('login')
