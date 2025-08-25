🎓 Student Management System

A simple Student Management System built with Streamlit (for the frontend) and MySQL (for the backend database).
This project allows an Admin to securely log in and manage student records (CRUD operations).

✨ Features

✅ Admin Login – Secure login system for administrators
✅ Add Student – Insert student details into the database
✅ View All Students – Display all student records in a table
✅ Update Marks – Modify a student’s marks
✅ Delete Student – Remove a student record
✅ Search Student – Find a student by name
✅ Logout – End admin session

🛠️ Tech Stack

Frontend: Streamlit

Backend: MySQL

Language: Python 3

📂 Database Schema
admin Table
Column	Type	Description
username	VARCHAR	Admin username
password	VARCHAR	Admin password (store hashed for security)
students Table
Column	Type	Description
id	INT (PK)	Auto-increment ID
name	VARCHAR	Student’s name
age	INT	Student’s age
course	VARCHAR	Student’s course
marks	INT	Marks (0–100)
🚀 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/student-management-system.git
cd student-management-system

2️⃣ Create Virtual Environment & Install Dependencies
pip install -r requirements.txt

3️⃣ Setup MySQL Database
CREATE DATABASE student_db;

USE student_db;

-- Admin Table
CREATE TABLE admin (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(255) NOT NULL
);

-- Students Table
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100),
    marks INT
);

-- Insert default admin
INSERT INTO admin (username, password) VALUES ("admin", "admin123");


(⚠️ For production, use hashed passwords instead of plain text.)

4️⃣ Run the App
streamlit run app.py



🔮 Future Improvements

✅ Secure password storage with bcrypt

✅ Dropdown selection for updating/deleting students

✅ Export student data to CSV/Excel

✅ Add graphical insights (marks distribution, course stats)

✅ Multi-admin support with roles

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

📜 License

This project is licensed under the MIT License.
