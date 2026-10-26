
print("=== Manufacturing Cost and Profitability Analysis ===")

product = input("Enter product name: ")
quantity = int(input("Enter production quantity: "))

material_cost = float(input("Enter material cost per unit: Rs. "))
labour_cost = float(input("Enter labour cost per unit: Rs. "))
wastage_percent = float(input("Enter wastage percentage: "))
machine_cost = float(input("Enter total machine cost: Rs. "))
selling_price = float(input("Enter selling price per unit: Rs. "))
profit_target = float(input("Enter target profit percentage: "))

if (quantity <= 0 or min(material_cost, labour_cost,
        machine_cost, selling_price, profit_target) < 0
        or not 0 <= wastage_percent <= 100):
    print("Invalid input!")
else:
    total_material = material_cost * quantity
    wastage_cost = total_material * wastage_percent / 100
    total_labour = labour_cost * quantity

    total_cost = (
        total_material + wastage_cost
        + total_labour + machine_cost
    )

    production_cost_per_unit = total_cost / quantity
    total_revenue = selling_price * quantity
    profit = total_revenue - total_cost

    if total_cost > 0:
        profit_percent = profit / total_cost * 100
    else:
        profit_percent = 0

    print("\n========== COST REPORT ==========")
    print("Product Name:", product)
    print("Production Quantity:", quantity)
    print(f"Material Cost: Rs. {total_material:.2f}")
    print(f"Wastage Cost: Rs. {wastage_cost:.2f}")
    print(f"Labour Cost: Rs. {total_labour:.2f}")
    print(f"Machine Cost: Rs. {machine_cost:.2f}")
    print(f"Total Production Cost: Rs. {total_cost:.2f}")
    print(f"Cost Per Unit: Rs. {production_cost_per_unit:.2f}")
    print(f"Total Revenue: Rs. {total_revenue:.2f}")
    print(f"Profit/Loss: Rs. {profit:.2f}")
    print(f"Profit Percentage: {profit_percent:.2f}%")

    if profit_percent >= profit_target:
        print("Status: Target Profit Achieved")
    else:
        print("Status: Target Profit Not Achieved")
