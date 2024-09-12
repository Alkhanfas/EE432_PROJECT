import json
import os


def search(course_name, students_data):
    result = {}
    for student_id, details in students_data.items():

        if course_name in details['currint_courses']:
            result[student_id] = details['Number_of_units']
    return result



def get_start(file_name):

    if os.path.exists(file_name):

        with open(file_name, 'r') as file:
            try:
                data_loaded = json.load(file)
            except json.JSONDecodeError:

                data_loaded = {}
    else:

        with open(file_name, 'w') as file:
            json.dump({}, file)


        data_loaded = {}

    return data_loaded


def save(students_data):
    with open('students.json', 'w') as file:
        json.dump(students_data, file, indent=4)



def available_terms(student_details, requirements_of_terms,currint_courses):
    valid_terms = []

    for term, requirements in requirements_of_terms.items():

        if term not in student_details:

            all_requirements_met = True
            for requirement in requirements:
                if requirement not in student_details:
                    all_requirements_met = False
                    break
            if all_requirements_met and term not in currint_courses:
                valid_terms.append(term)
    return valid_terms


def add_course(append_courses, list_of_terms, inputs, units_of_terms, student_data):
    n_unit = sum(units_of_terms.get(course, 0) for course in append_courses)
    for input in inputs:
        input = int(input) - 1
        term = list_of_terms[input]
        if term not in append_courses:
            n_unit += units_of_terms.get(term, 0)
            if n_unit > 18:
                print("\nYou can't register more than 18 units, courses above 18 units have been ignored!")
                return
            append_courses.append(term)
            students = search(term, student_data)

            if len(students) > 20:
                students = dict(sorted(students.items(), key=lambda item: item[1]))
                items = list(students.items())
                print(f"{term} is dropped for student with ID {items[0][0]} due to ")
                less_student = student_data[items[0][0]]["currint_courses"]
                for i , j in enumerate(less_student):
                    if j == term:
                        less_student.pop(i)
                        break




def drop_courses(current_courses, inputs):
    courses = current_courses[:]
    for index in inputs:
        index = int(index) - 1
        if 0 <= index < len(courses):
            courses[index] = None
    current_courses[:] = [course for course in courses if course is not None]



def get_number_of_units(currint_courses , units_of_terms):
    number_of_units = 0
    for course in currint_courses:
        number_of_units += units_of_terms[course]

    return number_of_units

def add_student(student_name, studentID,students_data):
    new_data = {
        studentID: {
            "student_name": student_name,
            "pass_terms": {},
            "semester_grades": {},
            "Number_of_units": 0,
            "currint_courses":[],
        }
    }
    if studentID not in students_data:
        students_data[studentID] = new_data[studentID]
    else:
        print(f"Student ID {studentID} is rely exist !")
    return students_data


def delete_student(studentID,students_data):
    del students_data[studentID]
    return students_data


def add_grade(grade,course,semester_grades,pass_term,units_of_terms):
    if float(grade) >= 50 :
        pass_term[course] = grade
        semester_grades[course] = grade
        return units_of_terms[course]

    semester_grades[course] = grade
    return 0

