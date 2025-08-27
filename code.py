import streamlit as st
import mysql.connector

# Initialize DB connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=""#your sql password,
        database=""#your database in which all the tables are stored
    )

# Admin login check
def login_admin(username, password):
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM admin WHERE username=%s AND password=%s", (username, password))
    result = cur.fetchone()
    cur.close()
    con.close()
    return result

# Add student
def add_student_db(name, age, course, marks):
    con = get_connection()
    cur = con.cursor()
    cur.execute("INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s)",
                (name, age, course, marks))
    con.commit()
    cur.close()
    con.close()

# View all students
def get_all_students():
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    results = cur.fetchall()
    cur.close()
    con.close()
    return results

# Search student
def search_student(name):
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM students WHERE name = %s", (name,))
    result = cur.fetchall()
    cur.close()
    con.close()
    return result

# Update marks
def update_student_marks(name, new_marks):
    con = get_connection()
    cur = con.cursor()
    cur.execute("UPDATE students SET marks = %s WHERE name = %s", (new_marks, name))
    con.commit()
    cur.close()
    con.close()

# Delete student
def delete_student(name):
    con = get_connection()
    cur = con.cursor()
    cur.execute("DELETE FROM students WHERE name = %s", (name,))
    con.commit()
    cur.close()
    con.close()

# Streamlit App
st.set_page_config(page_title="Student Manager", page_icon="🎓")
st.title("🎓 Student Management System")

# Session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Login screen
if not st.session_state.logged_in:
    st.subheader("🔐 Admin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login_admin(username, password):
            st.success("✅ Login successful")
            st.session_state.logged_in = True
        else:
            st.error("❌ Invalid credentials")

# Dashboard after login
else:
    menu = st.sidebar.selectbox("Select an action", ["Add Student", "View All", "Update Marks", "Delete Student", "Search", "Logout"])

    if menu == "Add Student":
        st.subheader("➕ Add Student")
        name = st.text_input("Student Name")
        age = st.number_input("Age", min_value=1, step=1)
        course = st.text_input("Course")
        marks = st.number_input("Marks", min_value=0, max_value=100, step=1)
        if st.button("Add"):
            add_student_db(name, age, course, marks)
            st.success("✅ Student added successfully!")

    elif menu == "View All":
        st.subheader("📄 All Student Records")
        records = get_all_students()
        if records:
            st.table(records)
        else:
            st.info("No student records found.")

    elif menu == "Update Marks":
        st.subheader("✏️ Update Marks")
        name = st.text_input("Student Name")
        new_marks = st.number_input("New Marks", min_value=0, max_value=100, step=1)
        if st.button("Update"):
            update_student_marks(name, new_marks)
            st.success("✅ Marks updated successfully")

    elif menu == "Delete Student":
        st.subheader("❌ Delete Student")
        name = st.text_input("Student Name to Delete")
        if st.button("Delete"):
            delete_student(name)
            st.warning("⚠️ Student record deleted!")

    elif menu == "Search":
        st.subheader("🔍 Search Student")
        name = st.text_input("Enter Student Name")
        if st.button("Search"):
            result = search_student(name)
            if result:
                st.table(result)
            else:
                st.error("❌ No student found.")

    elif menu == "Logout":
        st.session_state.logged_in = False
        st.success("🚪 Logged out successfully!")

