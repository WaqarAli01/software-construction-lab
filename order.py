def calculate_subtotal(items: list[dict[str, int]]) -> int:
    total = 0
    for item in items:
        price = item["price"]
        quantity = item["qty"]
        if price <= 0:
            continue
        if quantity <= 0:
            continue
        total = total + price * quantity
    return total

def calculate_discount(total: int, is_member: bool) -> float:
    if is_member != True:
        return 0
    if total > 100:
        return total * 0.2
    if total > 50:
        return total * 0.1
    return 0

def calculate_shipping(country: str) -> int:
    if country == "PK":
        return 5
    if country == "US":
        return 15
    return 25

def calculate_total(order: dict) -> float:
    subtotal = calculate_subtotal(order["items"])
    discount = calculate_discount(subtotal, order["member"])
    total = subtotal - discount
    shipping = calculate_shipping(order["country"])
    total = total + shipping
    print("Total: " + str(total))
    return total