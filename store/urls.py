
from django.contrib import admin
from django.urls import path
from .views import index, login, signup,cart

urlpatterns = [
    path('', index.Index.as_view(), name='homepage'),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('login', login.Login.as_view(), name='login'),
    path('logout', login.logout, name='logout'),
    path('cart',cart.Cart.as_view(),name='cart')
    path('check-out',)

]
