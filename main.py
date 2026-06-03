students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        roll = input("Enter Roll Number: ")

        students.append({
            "name": name,
            "roll": roll
        })

        print("Student Added Successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No Students Found")
        else:
            for s in students:
                print(f"Name: {s['name']} | Roll No: {s['roll']}")

    elif choice == "3":
        roll = input("Enter Roll Number: ")

        found = False

        for s in students:
            if s["roll"] == roll:
                print(f"Name: {s['name']}")
                found = True
                break

        if not found:
            print("Student Not Found")

    elif choice == "4":
        roll = input("Enter Roll Number to Delete: ")

        for s in students:
            if s["roll"] == roll:
                students.remove(s)
                print("Student Deleted")
                break

    elif choice == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
