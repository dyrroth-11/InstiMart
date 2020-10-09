from django.shortcuts import render
from store.models.product import Product
from store.models.category import Category

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
