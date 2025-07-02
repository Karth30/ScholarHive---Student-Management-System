import streamlit as st
from db.db_utils import insert_course

def render():
    st.header(" Add New Course")

    name = st.text_input("Course Name")
    instructor = st.text_input("Instructor Name")

    if st.button("Add Course"):
        insert_course(name, instructor)
        st.success("Course added successfully!")
