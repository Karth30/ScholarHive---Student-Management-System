import streamlit as st
import importlib.util
from db.db_utils import fetch_enrollments, get_all_students, get_all_courses
import pandas as pd
import plotly.express as px

# Streamlit page setup
st.set_page_config(page_title="ScholarHive", layout="wide")

# Login credentials
CREDENTIALS = {
    "admin": "admin",
    "user": "admin"
}

# Simple login logic
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title(" Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if CREDENTIALS.get(username) == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()
        else:
            st.error("Invalid credentials")
    st.stop()

# Sidebar
st.sidebar.title("ScholarHive")
page = st.sidebar.radio("Go to", [
    "Dashboard",
    "Add Student",
    "Add Course",
    "Enroll Student",
    "View Enrollments"
])

if st.sidebar.button("Logout"):
    st.session_state.clear()
    st.rerun()

# Dynamic loader
def load_and_run(filename):
    path = f"app_pages/{filename}"
    spec = importlib.util.spec_from_file_location("module.name", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.render()

# Routing
if page == "Dashboard":
    st.title(" Dashboard")
    students = get_all_students()
    courses = get_all_courses()
    enrollments = fetch_enrollments()

    col1, col2, col3 = st.columns(3)
    col1.metric("Students", len(students))
    col2.metric("Courses", len(courses))
    col3.metric("Enrollments", len(enrollments))

    df = pd.DataFrame(enrollments, columns=["Student", "Course", "Enrollment Date"])
    if not df.empty:
        fig = px.histogram(df, x="Course", title="Enrollments by Course")
        st.plotly_chart(fig)
    else:
        st.info("No enrollments to display.")
elif page == "Add Student":
    load_and_run("1_Add_Student.py")
elif page == "Add Course":
    load_and_run("2_Add_Course.py")
elif page == "Enroll Student":
    load_and_run("3_Enroll.py")
elif page == "View Enrollments":
    load_and_run("4_View_Data.py")
