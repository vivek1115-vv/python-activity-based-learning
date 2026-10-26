
def hospital_billing():
    print("=== Hospital Billing System ===")

    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))

    consultation = float(input("Enter consultation charges: Rs. "))
    diagnostic = float(input("Enter diagnostic charges: Rs. "))
    treatment = float(input("Enter treatment charges: Rs. "))

    if age < 0 or min(consultation, diagnostic, treatment) < 0:
        print("Invalid input! Age and charges cannot be negative.")
        return

    total = consultation + diagnostic + treatment

    # Conditional concession
    concession = 0

    if age >= 60:
        concession = total * 0.10
    elif total >= 10000:
        concession = total * 0.05

    final_bill = total - concession

    # Payment policy classification
    print("\n--- Patient Bill ---")
    print("Patient Name:", name)
    print("Consultation Charges: Rs.", consultation)
    print("Diagnostic Charges: Rs.", diagnostic)
    print("Treatment Charges: Rs.", treatment)
    print("Total Charges: Rs.", total)
    print("Concession: Rs.", round(concession, 2))
    print("Final Bill: Rs.", round(final_bill, 2))

    if final_bill <= 0:
        print("Invalid billing amount.")
    elif final_bill < 5000:
        print("Patient Classification: Standard")
    elif final_bill < 20000:
        print("Patient Classification: Intermediate")
    else:
        print("Patient Classification: High-Cost")

    payment = input("\nPayment status (Paid/Unpaid): ").strip().lower()

    if payment == "paid":
        print("Payment Status: Completed")
    elif payment == "unpaid":
        print("Payment Status: Pending")
    else:
        print("Invalid payment status!")


hospital_billing()
