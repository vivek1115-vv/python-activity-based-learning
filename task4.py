
def calculate_payroll():
    print("=== Employee Payroll System ===")

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")

    basic = float(input("Enter Basic Pay: Rs. "))
    allowances = float(input("Enter Allowances: Rs. "))
    overtime_hours = float(input("Enter Overtime Hours: "))
    overtime_rate = float(input("Enter Overtime Rate per Hour: Rs. "))
    incentives = float(input("Enter Incentives: Rs. "))

    if min(basic, allowances, overtime_hours,
           overtime_rate, incentives) < 0:
        print("Invalid input! Values cannot be negative.")
        return

    overtime_pay = overtime_hours * overtime_rate
    gross_salary = basic + allowances + overtime_pay + incentives

    # Progressive deductions (example rates)
    if gross_salary <= 15000:
        deduction = gross_salary * 0.05
    elif gross_salary <= 30000:
        deduction = 15000 * 0.05 + (gross_salary - 15000) * 0.10
    else:
        deduction = (15000 * 0.05
                     + 15000 * 0.10
                     + (gross_salary - 30000) * 0.15)

    net_salary = gross_salary - deduction

    print("\n========== SALARY STATEMENT ==========")
    print("Employee ID       :", emp_id)
    print("Employee Name     :", name)
    print("--------------------------------------")
    print(f"Basic Pay         : Rs. {basic:.2f}")
    print(f"Allowances        : Rs. {allowances:.2f}")
    print(f"Overtime Pay      : Rs. {overtime_pay:.2f}")
    print(f"Incentives        : Rs. {incentives:.2f}")
    print("--------------------------------------")
    print(f"Gross Salary      : Rs. {gross_salary:.2f}")
    print(f"Total Deductions  : Rs. {deduction:.2f}")
    print(f"Net Salary        : Rs. {net_salary:.2f}")
    print("======================================")


calculate_payroll()
