
def calculate_subtotal(items):
    total = 0
    for item in items:
        price = item["price"]
        quantity = item["qty"]
        if price > 0:
            if quantity > 0:
                total = total + price * quantity
    return total

def calculate_discount(total, is_member):
    if is_member == True:
        if total > 100:
            discount = total * 0.2
        else:
            if total > 50:
                discount = total * 0.1
            else:
                discount = 0
    else:
        discount = 0
    return discount

def calculate_shipping(country):
    if country == "PK":
        shipping = 5
    else:
        if country == "US":
            shipping = 15
        else:
            shipping = 25
    return shipping

def calculate_total(order):
    subtotal = calculate_subtotal(order["items"])
    discount = calculate_discount(subtotal, order["member"])
    total = subtotal - discount
    shipping = calculate_shipping(order["country"])
    total = total + shipping
    print("Total: " + str(total))
    return total

