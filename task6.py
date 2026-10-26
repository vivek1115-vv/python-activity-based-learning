
def calculate_fare(distance, travel_class):
    rates = {
        "Sleeper": 1.0,
        "3AC": 2.0,
        "2AC": 3.0,
        "1AC": 4.0
    }

    if distance <= 100:
        slab_charge = distance * 1
    elif distance <= 500:
        slab_charge = 100 + (distance - 100) * 1.5
    else:
        slab_charge = 100 + 400 * 1.5 + (distance - 500) * 2

    return slab_charge * rates[travel_class]


print("=== Railway Fare and Reservation Calculator ===")

n = int(input("Enter number of passengers: "))
passengers = []

for i in range(n):
    print(f"\nPassenger {i + 1}")

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = float(input("Enter journey distance (km): "))

    print("Classes: Sleeper, 3AC, 2AC, 1AC")
    travel_class = input("Enter travel class: ").strip()

    if age < 0 or distance <= 0:
        print("Invalid age or distance!")
        continue

    if travel_class not in ["Sleeper", "3AC", "2AC", "1AC"]:
        print("Invalid travel class!")
        continue

    fare = calculate_fare(distance, travel_class)

    # Age-based concessions (example policy)
    concession = 0

    if age < 5:
        concession = fare       # Free fare
    elif age >= 60:
        concession = fare * 0.20

    reservation_fee = 40
    total = fare - concession + reservation_fee

    passengers.append({
        "name": name,
        "age": age,
        "fare": fare,
        "concession": concession,
        "fee": reservation_fee,
        "total": total
    })

    print("\n--- Ticket Details ---")
    print("Passenger:", name)
    print("Base Fare: Rs.", round(fare, 2))
    print("Concession: Rs.", round(concession, 2))
    print("Reservation Fee: Rs.", reservation_fee)
    print("Total Fare: Rs.", round(total, 2))

print("\n=== Reservation Summary ===")

grand_total = sum(p["total"] for p in passengers)

for p in passengers:
    print(p["name"], "- Rs.", round(p["total"], 2))

print("Total Booking Amount: Rs.", round(grand_total, 2))

if passengers:
    cancel = input("\nCancel a ticket? (yes/no): ").strip().lower()

    if cancel == "yes":
        name = input("Enter passenger name to cancel: ")
        passenger = next(
            (p for p in passengers if p["name"].lower() == name.lower()),
            None
        )

        if passenger:
            penalty = passenger["total"] * 0.25
            refund = passenger["total"] - penalty

            print("Cancellation Penalty: Rs.", round(penalty, 2))
            print("Refund Amount: Rs.", round(refund, 2))
        else:
            print("Passenger not found.")
