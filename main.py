import mysql.connector

# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Naresh@12",
    database="student_management"
)

cursor = conn.cursor()

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. View Students")
    print("2. Search Student")
    print("3. Add Student")
    print("4. Update Grade")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    # View Students
    if choice == "1":
        cursor.execute("SELECT * FROM students LIMIT 20")
        records = cursor.fetchall()

        print("\nStudent Records:")
        for row in records:
            print(row)

    # Search Student
    elif choice == "2":
        sid = int(input("Enter Student ID: "))

        cursor.execute(
            "SELECT * FROM students WHERE student_id=%s",
            (sid,)
        )

        result = cursor.fetchone()

        if result:
            print("\nStudent Found:")
            print(result)
        else:
            print("Student Not Found")

    # Add Student
    elif choice == "3":

        cursor.execute("SELECT MAX(student_id) FROM students")
        max_id = cursor.fetchone()[0]

        if max_id is None:
            student_id = 1
        else:
            student_id = max_id + 1

        print("Generated Student ID:", student_id)

        study_hours = float(input("Weekly Study Hours: "))
        attendance = float(input("Attendance Percentage: "))
        participation = float(input("Class Participation: "))
        total_score = float(input("Total Score: "))
        grade = input("Grade: ")

        try:
            cursor.execute("""
            INSERT INTO students
            (student_id,
             weekly_self_study_hours,
             attendance_percentage,
             class_participation,
             total_score,
             grade)
            VALUES (%s,%s,%s,%s,%s,%s)
            """,
            (
                student_id,
                study_hours,
                attendance,
                participation,
                total_score,
                grade
            ))

            conn.commit()

            print(f"Student {student_id} Added Successfully!")

        except Exception as e:
            print("Error:", e)

    # Update Grade
    elif choice == "4":
        sid = int(input("Enter Student ID: "))
        new_grade = input("Enter New Grade: ")

        cursor.execute("""
        UPDATE students
        SET grade=%s
        WHERE student_id=%s
        """,
        (
            new_grade,
            sid
        ))

        conn.commit()

        if cursor.rowcount > 0:
            print("Grade Updated Successfully!")
        else:
            print("Student Not Found")

    # Delete Student
    elif choice == "5":
        sid = int(input("Enter Student ID to Delete: "))

        cursor.execute(
            "DELETE FROM students WHERE student_id=%s",
            (sid,)
        )

        conn.commit()

        if cursor.rowcount > 0:
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found")

    # Exit
    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")

cursor.close()
conn.close()