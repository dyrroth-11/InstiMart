from django import template

register = template.Library()


@register.filter(name='currency')
def currency(num):
    return  "₹" +str(num);


@register.filter(name='multiply')
def multiply(x,y):
    return x*y
