import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        database="student_management"
    )

    cursor = conn.cursor()

    print("Database Connected Successfully!")

except mysql.connector.Error as err:
    print("Database Connection Error:")
    print(err)
