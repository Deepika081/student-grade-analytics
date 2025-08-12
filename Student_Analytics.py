# Student Grades & Analytics System

stud_data = {}       # {(roll_no, name): [marks]}
roll_no = {}         # {roll_no: name}
total_marks = {}     # {roll_no: total_score}
failed_stud = {}     # {name: failed_subject}

while True:
    print("\n===== Student Grades Management =====")
    print("1. Enter Data")
    print("2. Fetch Details")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\n--- Enter Student Data ---")
        roll_number = int(input("Enter Roll Number: "))

        if roll_number in roll_no:
            print("Roll number already exists!")
            continue

        name = input("Enter name of the student: ")

        roll_no[roll_number] = name
        student_key = (roll_number, name)

        print("Enter marks in order")
        marks = []
        subjects = ["Math", "Science", "English"]
        for subject in subjects:
            marks.append(int(input(f"{subject}: ")))

        stud_data[student_key] = marks
        total_marks[roll_number] = sum(marks)

        # Check if student failed in any subject
        sub = None
        if min(marks) < 40:
            fail_index = marks.index(min(marks))
            if fail_index == 0:
                sub = "Math"
            elif fail_index == 1:
                sub = "Science"
            else:
                sub = "English"
        if sub is not None:
            failed_stud[name] = sub

        print("Student data added successfully.")

    elif choice == 2:
        if not stud_data:
            print("\nPlease enter data first.")
        else:
            print("\n--- Fetch Details ---")
            print("1. Student Report")
            print("2. Class Analytics")
            fetch_choice = int(input("Enter your choice: "))

            if fetch_choice == 1:
                print("\nEnter Student Details to Fetch Report")
                temp_name = input("Name: ")
                temp_roll = int(input("Roll Number: "))
                student_key = (temp_roll, temp_name)

                if student_key in stud_data:
                    print(f"\nStudent Report: {temp_name} ({temp_roll})")
                    print(f"Math: {stud_data[student_key][0]}")
                    print(f"Science: {stud_data[student_key][1]}")
                    print(f"English: {stud_data[student_key][2]}")
                else:
                    print("No record found for this student.")

            elif fetch_choice == 2:
                print("\nClass Analytics")
                highest_scorer_id = max(total_marks, key=total_marks.get)
                print(f"Highest Marks: {roll_no[highest_scorer_id]} - {total_marks[highest_scorer_id]}")
                print(f"Class Average: {sum(total_marks.values()) / len(total_marks):.2f}")

                if failed_stud:
                    print("\nStudents Failed:")
                    for student, subject in failed_stud.items():
                        print(f"{student} → {subject}")
                else:
                    print("\nNo students have failed.")
            else:
                print("Invalid choice.")

    elif choice == 3:
        print("\nEnd of program. Goodbye!")
        break

    else:
        print("Invalid choice. Please select from the menu.")
