AI-Based-Placement-Prediction-System

 1. Approved Project Title
AI-Based Placement Prediction and Career Guidance System Using Machine Learning
2. Problem Statement
Many students are unaware of their placement readiness and lack guidance regarding the skills required for securing jobs. Existing systems only store academic records and do not provide intelligent insights. This project aims to analyze student academic performance, technical skills, aptitude scores, and other factors to predict placement chances and provide personalized career guidance using Machine Learning.
3. Project Objectives
Primary Objectives
Predict student placement probability using ML.
Analyze academic and skill-related factors.
Provide career guidance recommendations.
Help students identify skill gaps.
Secondary Objectives
Maintain student records.
Generate placement analytics.
Improve placement preparation.
4. Module List
Admin Module
Login
Manage Students
View Predictions
Manage Skills
Generate Reports
Student Module
Registration
Login
Profile Management
Skill Entry
View Prediction
ML Prediction Module
Data Processing
Model Training
Prediction Generation
Recommendation Module
Skill Suggestions
Career Guidance
Dashboard Module
Statistics
Placement Analytics
Charts and Reports
5. Use Case Diagram
Actors
Admin
Student
Use Cases
Student
Register
Login
Update Profile
Enter Skills
View Placement Prediction
View Recommendations
Admin
Login
Manage Students
Manage Data
View Reports
View Analytics
Simple Use Case Structure:

Admin ----> Login
      ----> Manage Students
      ----> View Reports
      ----> View Analytics

Student --> Register
        --> Login
        --> Update Profile
        --> Enter Skills
        --> View Prediction
        --> View Recommendations
6. Table List
Users
Students
Skills
Prediction
Recommendations
Admin
7. ER Diagram

ADMIN
 |
 |
STUDENT ----- SKILLS
 |
 |
PREDICTION
 |
 |
RECOMMENDATION
Relationship:
One Student → Many Skills
One Student → One Prediction
One Student → Many Recommendations
8. SQL Schema
Student Table
SQL
CREATE TABLE students(
student_id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(100),
email VARCHAR(100),
department VARCHAR(50),
cgpa DECIMAL(3,2),
attendance DECIMAL(5,2),
aptitude_score INT,
technical_score INT,
communication_score INT
);
Skills Table
SQL
CREATE TABLE skills(
skill_id INT PRIMARY KEY AUTO_INCREMENT,
student_id INT,
skill_name VARCHAR(100),
FOREIGN KEY(student_id)
REFERENCES students(student_id)
);
Prediction Table
SQL
CREATE TABLE prediction(
prediction_id INT PRIMARY KEY AUTO_INCREMENT,
student_id INT,
placement_probability DECIMAL(5,2),
status VARCHAR(20),
FOREIGN KEY(student_id)
REFERENCES students(student_id)
);
9. Page Layouts
Home Page
About Project
Features
Login
Register
Student Dashboard
Profile
Skills
Prediction
Recommendations
Admin Dashboard
Student List
Analytics
Reports
10. UI Screens
Screen 1
Home Page
Screen 2
Login Page
Screen 3
Registration Page
Screen 4
Student Dashboard
Screen 5
Prediction Result Page
Screen 6
Admin Dashboard
Screen 7
Analytics Dashboard
11. UI Prototype
Navigation

Home
 |
 +-- Login
 |
 +-- Register
 |
 +-- Dashboard
       |
       +-- Profile
       +-- Skills
       +-- Prediction
       +-- Recommendation
12. Technology Stack
Frontend
React JS
HTML
CSS
Bootstrap
Backend
Spring Boot
Java
Database
MySQL
Machine Learning
Python
Scikit-Learn
Pandas
NumPy
13. ML Model
Input Parameters
CGPA
Attendance
Aptitude Score
Technical Skills Score
Communication Skills Score
Projects Completed
Output

Placement Probability = 85%

Status = Likely to be Placed
Algorithm
Random Forest Classifier
Reason:
High accuracy
Easy implementation
Good for student datasets
Frontend Pages Needed
Home
Login
Registration
Student Dashboard
Profile Form
Skill Entry Form
Prediction Page
Recommendation Page
Admin Dashboard
Student List