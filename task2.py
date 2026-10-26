
def calculate_bill(units):
    bill = 0

    if units <= 100:
        bill = units * 1.50
    elif units <= 200:
        bill = 100 * 1.50 + (units - 100) * 2.50
    elif units <= 300:
        bill = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4.00
    else:
        bill = 100 * 1.50 + 100 * 2.50 + 100 * 4.00 + (units - 300) * 6.00

    fixed_charge = 50
    surcharge = bill * 0.05
    rebate = 20 if units <= 100 else 0

    total = bill + fixed_charge + surcharge - rebate
    return round(total, 2)


months = int(input("Enter number of months: "))
bills = []

for i in range(months):
    print(f"\nMonth {i + 1}")
    units = float(input("Enter electricity units: "))
    bill = calculate_bill(units)
    bills.append(bill)

    print("Electricity Bill: Rs.", bill)

print("\n--- Monthly Bill Comparison ---")

for i in range(months):
    print(f"Month {i + 1}: Rs. {bills[i]}")

    if i > 0 and bills[i] > bills[i - 1] * 1.25:
        print("Warning: Unusual bill increase detected!")

print("\nBilling analysis completed.")
