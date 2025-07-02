import streamlit as st
from db.db_utils import fetch_enrollments

def render():
    st.header(" View Enrollments")

    data = fetch_enrollments()

    if data:
        st.table(data)
    else:
        st.info("No enrollments found.")
