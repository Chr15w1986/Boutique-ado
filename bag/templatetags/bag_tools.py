""" Corrects the subtotal shown in the bag to the quantity of items """
from django import template

register = template.Library()


@register.filter('calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
