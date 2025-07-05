# ScholarHive — Student Management System

ScholarHive is a lightweight student-course enrollment management system built with Streamlit and backed by a MySQL database.  
It features user authentication, student and course management, enrollment tracking, and a data dashboard with interactive visualizations.

---

## Features

- User login and logout  
- Add and view students  
- Add and view courses  
- Enroll students into courses  
- Dashboard with enrollment insights using Plotly  
- MySQL backend with persistent storage  
- Clean modular structure with Streamlit sidebar navigation

---

## Folder Structure

```
ScholarHive/
├── app.py                  # Main Streamlit app
├── db/
│   ├── config.py           # MySQL credentials
│   └── db_utils.py         # Database operations
├── app_pages/
│   ├── 1_Add_Student.py
│   ├── 2_Add_Course.py
│   ├── 3_Enroll.py
│   └── 4_View_Data.py
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Install Requirements

```
pip install -r requirements.txt
```

### 2. Set Up MySQL Database

Create a database named `student_db`:

```
CREATE DATABASE student_db;
```

Inside `db/config.py`, set your MySQL credentials:

```
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "your_mysql_password"
DB_NAME = "student_db"
```

Create the required tables:

```
USE student_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    dob DATE
);

CREATE TABLE courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100),
    instructor VARCHAR(100)
);

CREATE TABLE enrollments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
```

### 3. Run the App

```
streamlit run app.py
```

Default login credentials (defined in `app.py`):

```
CREDENTIALS = {
    "admin": "admin",
    "user": "admin"
}
```

---

## Dependencies

Listed in `requirements.txt`:

```
streamlit
mysql-connector-python
pandas
plotly
```

---

## Application Preview

![image](https://github.com/user-attachments/assets/1b7ea009-9e0d-4c29-a699-585966449f88)

![image](https://github.com/user-attachments/assets/1afe2143-9506-4632-ad70-7a5baf53cee8)

![image](https://github.com/user-attachments/assets/95db1491-75b7-410f-826b-75fd8b3ec82f)

![image](https://github.com/user-attachments/assets/79f283c2-2351-4306-9dec-60138be182ec)

![image](https://github.com/user-attachments/assets/a20700ef-7494-43d8-9827-f64a3f6cf875)

![image](https://github.com/user-attachments/assets/df1ca337-9171-4ca2-9cc7-26fbc009ac01)





---

