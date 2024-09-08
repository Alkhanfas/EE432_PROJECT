import json
import os

def add_student(student_name, studentID):
    new_data = {
        studentID: {
            "student_name": student_name,
            "pass_terms": {},
            "Number_of_units": 0,
        }
    }

    if os.path.exists('students.json'):

        with open('students.json', 'r') as file:
            try:
                data_loaded = json.load(file)
            except json.JSONDecodeError:
                data_loaded = {}
    else:

        data_loaded = {}

    if studentID not in data_loaded:

        data_loaded[studentID] = new_data[studentID]
        with open('students.json', 'w') as file:
            json.dump(data_loaded, file, indent=4)
    else:
        print(f"Student ID {studentID} is rely exist !")

def delete_student(studentID):

    if os.path.exists('students.json'):
        with open('students.json', 'r') as file:
            try:
                data_loaded = json.load(file)
            except json.JSONDecodeError:
                data_loaded = {}
    else:
        data_loaded = {}

    if studentID in data_loaded:
        del data_loaded[studentID]

        with open('students.json', 'w') as file:
            json.dump(data_loaded, file, indent=4)
        print(f"student with ID : {studentID} removed successful .")
    else:
        print(f"there is no student with ID : {studentID} to remove !.")
