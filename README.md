<h1></h1>

<div align="center">
<h1>Tripoli University EEE department administration System</h1>
<img src="photos/3.png" alt="University Logo" style="width: 350px;"/>



</div>

## Overview
This project is a university management system specifically designed for the Department of Electrical and Electronics Engineering. The main goal of the system is to electronically and easily manage students, courses, and grades.

## Key Features
- **Student Management**: Add, edit, view, and delete student information.
- **Course Management**: Add, view, and delete course information.
- **Grade Management**: Add and view student grades for each course.

## Prerequisites
- Python 3.x
- `json` library (for handling data files)
- `os` library (for system-related operations)

## How to Run

1. To run the system, use the following command:
    ```bash
    python app.py
    ```

## File Structure
- `students.json`: Contains student data (student ID, name, and number of units).
- `units_of_terms.json`: Contains course data (course ID and number of units).
- `requirements.json`: Contains courses and their requirements.

## Usage
### Student Management
1. **Add Student** : Enter the student ID and name to add a new student.
2. **Register for a new semester**: You clear the record for the current semester and register for a new semester.
3. **View Students** : Displays a list of all registered students.
4. **Student Details** : Displays detailed information about the student, including grades and enrolled courses.
5. **remove student** : Removes all student data.
 
### Course Management
1. **Add Course**: Add a new course by entering student ID and the available courses.
-  `Note` : The maximum number of students to register for a course is 20, and priority in downloading the course is given to those with the largest number of completed units to change it go to :
**usage.py - > add_course function - > if len(students) > 20:**
2. **View Courses**: Displays a list of all registered courses for the student.
3. **Drop Course**: Drop a recorded item.

### Grade Management
1. **Add Grades**: Add grades for students based on the courses they are enrolled in.
2. **View Grades**: Displays the grades of a student for each enrolled course.

## Contributors
[Mohammed Al-khanfas](https://t.me/MedooKn) <h6></h6> [Ahmed Swisi](https://t.me/Ahmed_swisi2318)  <h6></h6> [Hammam maroof](https://t.me/hummam29)  <h6></h6> [Abdulrahman Al-mazoughi](https://t.me/)

