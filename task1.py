
n = int(input("Enter number of applicants: "))

students = []

for i in range(n):
    print("\nApplicant", i + 1)

    name = input("Enter name: ")
    marks = float(input("Enter aggregate marks: "))
    s1 = float(input("Enter subject 1 marks: "))
    s2 = float(input("Enter subject 2 marks: "))
    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    if (marks >= 75 and s1 >= 40 and s2 >= 40
            and attendance >= 75 and income <= 250000):
        students.append((name, marks, attendance, income))
        print("Eligible")
    else:
        print("Not Eligible")

# Rank by marks, attendance, lower income, then name
students.sort(key=lambda x: (-x[1], -x[2], x[3], x[0].lower()))

print("\n--- Scholarship Merit List ---")

if students:
    for rank, student in enumerate(students, 1):
        print(rank, student[0],
              "Marks:", student[1],
              "Attendance:", student[2],
              "Income:", student[3])
else:
    print("No eligible applicants")
