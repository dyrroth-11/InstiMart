from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for key in keys:
        if int(key) == product.id:
            return True
    return False
