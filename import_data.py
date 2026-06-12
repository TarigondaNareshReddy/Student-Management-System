import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Naresh@12",
    database="student_management"
)

cursor = conn.cursor()

print("Import Started...")

df = pd.read_csv("student_performance.csv")

print("Rows found:", len(df))

for index, row in df.iterrows():

    print("Inserting row", index + 1)

    sql = """
    INSERT INTO students
    (
        student_id,
        weekly_self_study_hours,
        attendance_percentage,
        class_participation,
        total_score,
        grade
    )
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    values = (
        row["student_id"],
        row["weekly_self_study_hours"],
        row["attendance_percentage"],
        row["class_participation"],
        row["total_score"],
        row["grade"]
    )

    cursor.execute(sql, values)

conn.commit()

print("Dataset Imported Successfully!")

cursor.close()
conn.close()