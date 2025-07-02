# db/db_utils.py
import mysql.connector
from db.config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def insert_student(name, email, dob):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, email, dob) VALUES (%s, %s, %s)", (name, email, dob))
    conn.commit()
    conn.close()

def insert_course(name, instructor):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO courses (course_name, instructor) VALUES (%s, %s)", (name, instructor))
    conn.commit()
    conn.close()

def enroll_student(student_id, course_id, date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES (%s, %s, %s)", (student_id, course_id, date))
    conn.commit()
    conn.close()

def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM students")
    data = cursor.fetchall()
    conn.close()
    return data

def get_all_courses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, course_name FROM courses")
    data = cursor.fetchall()
    conn.close()
    return data

def fetch_enrollments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.name, c.course_name, e.enrollment_date
        FROM enrollments e
        JOIN students s ON e.student_id = s.id
        JOIN courses c ON e.course_id = c.id
    """)
    result = cursor.fetchall()
    conn.close()
    return result
