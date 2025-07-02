import streamlit as st
from db.db_utils import get_all_students, get_all_courses, enroll_student
from datetime import date

def render():
    st.header(" Enroll Student in Course")

    students = get_all_students()
    courses = get_all_courses()

    student_dict = {name: sid for sid, name in students}
    course_dict = {cname: cid for cid, cname in courses}

    if not student_dict or not course_dict:
        st.warning("Add students and courses first.")
        return

    student_name = st.selectbox("Select Student", list(student_dict.keys()))
    course_name = st.selectbox("Select Course", list(course_dict.keys()))
    enroll_date = st.date_input("Enrollment Date", value=date.today())

    if st.button("Enroll"):
        enroll_student(student_dict[student_name], course_dict[course_name], enroll_date)
        st.success(f"{student_name} enrolled in {course_name}.")
