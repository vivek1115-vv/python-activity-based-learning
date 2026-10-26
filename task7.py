
print("=== Retail Billing System ===")

n = int(input("Enter number of products: "))

subtotal = 0
total_tax = 0
items = []

for i in range(n):
    print(f"\nProduct {i + 1}")

    name = input("Enter product name: ")
    category = input("Enter category (food/clothing/electronics): ").lower()
    price = float(input("Enter price per unit: Rs. "))
    quantity = int(input("Enter quantity: "))

    if price < 0 or quantity <= 0:
        print("Invalid price or quantity!")
        continue

    amount = price * quantity

    # Category-specific tax rates (example)
    if category == "food":
        tax_rate = 5
    elif category == "clothing":
        tax_rate = 8
    elif category == "electronics":
        tax_rate = 18
    else:
        print("Unknown category! Using 0% tax.")
        tax_rate = 0

    tax = amount * tax_rate / 100

    items.append({
        "name": name,
        "quantity": quantity,
        "amount": amount,
        "tax": tax,
        "tax_rate": tax_rate
    })

    subtotal += amount
    total_tax += tax

# Threshold discount rules
if subtotal >= 10000:
    discount_rate = 15
elif subtotal >= 5000:
    discount_rate = 10
elif subtotal >= 2000:
    discount_rate = 5
else:
    discount_rate = 0

discount = subtotal * discount_rate / 100

# Maximum concession limit
max_concession = 1500
discount = min(discount, max_concession)

final_total = subtotal + total_tax - discount

# Itemized invoice
print("\n========== ITEMIZED INVOICE ==========")
print(f"{'Product':15} {'Qty':>4} {'Amount':>10} {'Tax':>8}")

for item in items:
    print(f"{item['name']:15} {item['quantity']:>4} "
          f"{item['amount']:>10.2f} {item['tax']:>8.2f}")

print("--------------------------------------")
print(f"Subtotal       : Rs. {subtotal:.2f}")
print(f"Total Tax      : Rs. {total_tax:.2f}")
print(f"Discount       : Rs. {discount:.2f}")
print(f"Final Bill     : Rs. {final_total:.2f}")
print("======================================")
