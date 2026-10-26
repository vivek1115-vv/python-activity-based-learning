
print("=== Mobile Plan Cost Optimization ===")

budget = float(input("Enter your budget (Rs.): "))
required_validity = int(input("Enter required validity (days): "))
required_data = float(input("Enter required data (GB): "))
required_calls = int(input("Enter required calls (minutes): "))

plans = [
    {"name": "Plan A", "price": 199, "validity": 28,
     "data": 1, "calls": 500, "extra_data": 20, "extra_call": 0.50},

    {"name": "Plan B", "price": 299, "validity": 56,
     "data": 2, "calls": 1000, "extra_data": 15, "extra_call": 0.40},

    {"name": "Plan C", "price": 399, "validity": 84,
     "data": 3, "calls": 1500, "extra_data": 10, "extra_call": 0.30}
]

eligible_plans = []

for plan in plans:
    if plan["validity"] < required_validity:
        continue

    if plan["price"] > budget:
        continue

    extra_data = max(0, required_data - plan["data"])
    extra_calls = max(0, required_calls - plan["calls"])

    excess_charge = (
        extra_data * plan["extra_data"]
        + extra_calls * plan["extra_call"]
    )

    total_cost = plan["price"] + excess_charge

    eligible_plans.append({
        "name": plan["name"],
        "price": plan["price"],
        "excess": excess_charge,
        "total": total_cost
    })

print("\n=== Plan Comparison ===")

if not eligible_plans:
    print("No plan satisfies the budget and validity constraints.")
else:
    for plan in eligible_plans:
        print("\nPlan:", plan["name"])
        print("Base Price: Rs.", plan["price"])
        print("Excess Charges: Rs.", round(plan["excess"], 2))
        print("Total Cost: Rs.", round(plan["total"], 2))

    best_plan = min(eligible_plans, key=lambda p: p["total"])

    print("\n=== Most Economical Plan ===")
    print("Plan:", best_plan["name"])
    print("Total Cost: Rs.", round(best_plan["total"], 2))
