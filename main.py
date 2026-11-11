
students = []
companies = []
placements = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    cgpa = float(input("Enter CGPA: "))
    skills = input("Enter skills: ")

    students.append({
        "name": name,
        "roll": roll,
        "cgpa": cgpa,
        "skills": skills
    })
    print("Student registered successfully!")

def add_company():
    name = input("Enter company name: ")
    package = input("Enter salary package: ")

    companies.append({
        "name": name,
        "package": package
    })
    print("Company registered successfully!")

def check_eligibility():
    for student in students:
        status = "Eligible" if student["cgpa"] >= 7.0 else "Not Eligible"
        print(student["name"], "-", status)

def schedule_interview():
    roll = input("Enter student roll number: ")
    company = input("Enter company name: ")
    date = input("Enter interview date: ")

    placements.append({
        "roll": roll,
        "company": company,
        "date": date
    })
    print("Interview scheduled successfully!")

def placement_report():
    print("\n--- Student Details ---")
    for student in students:
        print(student)

    print("\n--- Company Details ---")
    for company in companies:
        print(company)

    print("\n--- Interview Details ---")
    for placement in placements:
        print(placement)

while True:
    print("\n===== STUDENT PLACEMENT MANAGEMENT =====")
    print("1. Student Profile")
    print("2. Company Registration")
    print("3. Eligibility Checking")
    print("4. Interview Scheduling")
    print("5. Placement Reports")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        add_company()
    elif choice == "3":
        check_eligibility()
    elif choice == "4":
        schedule_interview()
    elif choice == "5":
        placement_report()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
