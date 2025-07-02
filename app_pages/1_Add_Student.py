# pages/1_Add_Student.py
import streamlit as st
from db.db_utils import insert_student

def render():
    st.header(" Add New Student")

    name = st.text_input("Student Name")
    email = st.text_input("Email")
    dob = st.date_input("Date of Birth")

    if st.button("Add Student"):
        insert_student(name, email, dob)
        st.success("Student added successfully!")
