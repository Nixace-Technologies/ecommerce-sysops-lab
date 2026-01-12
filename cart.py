from products import PRODUCTS

def calculate_total(cart_items):
    total = 0
    for item in cart_items:
        if item in PRODUCTS:
            total += PRODUCTS[item]
    return total
