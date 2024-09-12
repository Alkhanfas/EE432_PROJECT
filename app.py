from usage import *

students_data = get_start('students.json')
requirements_of_terms = get_start("requirements.json")
units_of_terms = get_start("units_of_terms.json")


while True :
    print("\n Tripoli University EEE department administration System : ")
    print("1. Manage Students")
    print("2. Manage Courses")
    print("3. Manage Grades")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        while True:
            print("\nManage Students")
            print("1. Add Student")
            print("2. start new semester")
            print("3. List Students")
            print("4. Student details ")
            print("5. remove student")
            print("6. save changes")
            print("7. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                studentID = input("Enter student ID: ")
                if studentID in students_data:
                    print("\n Student ID already exist")
                else:
                    student_name = input("Enter student name: ")
                    add_student(student_name, studentID, students_data)
                    print("\n Student has been added successfully")
                    save_change = True
            elif choice == '2':
                studentID = input("Enter student ID: ")
                try :
                    students_data[studentID]["semester_grades"] ={}
                    print("\n A New semester has been successfully opened")
                    save_change = True
                except KeyError :
                    print(f"\n no student with ID : {studentID} ")

            elif choice == '3':
                for i in students_data:
                    print(f"student ID :{i}  student name :{students_data[i]["student_name"]}  Number_of_units : {students_data[i]["Number_of_units"]} ")

            elif choice == '4':
                try :
                    student_id = input("Enter student ID: ")
                    print(f"student ID :{student_id}  student name :{students_data[student_id]["student_name"]}  Number_of_units : {students_data[student_id]["Number_of_units"]} ")
                    print("pass terms :")
                    for term , grade in students_data[student_id]["pass_terms"].items():
                        print(f"course : {term} -> {grade} ")
                    print ("currint semester grades:")
                    for term , grade in students_data[student_id]["semester_grades"].items():
                        print(f"course : {term} -> {grade} ")
                except KeyError :
                    print(f"\n no student with ID : {studentID} ")

            elif choice =="5":
                studentID = input("Enter student ID: ")
                try :
                    delete_student(studentID,students_data)
                    save_change = True
                    print("\n The student’s registration has been successfully canceled")
                except KeyError :
                    print(f"\n no student with ID : {studentID} ")

            elif choice == "6":
                save(students_data)
                print("\n All changes have been saved")
                save_change = False

            elif choice == '7':
                try:
                    if save_change == True:
                        ans = input("\n do you want to save changes press yes/no :")
                        if ans == "yes":
                            save(students_data)
                    save_change = False
                    break
                except NameError:
                    break


            else:
                print("\n Invalid choice. Please try again.")

    if choice == '2':
        while True:
            print("\nManage Courses: ")
            print("1. Add Course")
            print("2. List Courses")
            print("3. Drop course ")
            print("4. Save changes ")
            print("5. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                student_id = input("Enter student ID: ")
                try :
                    list_of_terms = available_terms(students_data[student_id]["pass_terms"],requirements_of_terms,students_data[student_id]["currint_courses"])
                    print("\nthe available courses : ")
                    for i,term in enumerate(list_of_terms):
                        print(f"{i+1}. {term}")
                    inputs = input("select courses by numbers separated by space : ").split()

                    try:
                        add_course(students_data[student_id]["currint_courses"],list_of_terms,inputs,units_of_terms,students_data)
                    except IndexError :
                        print("\n invalid inputs try again !")
                    save_change = True


                except KeyError :
                    print("\ninvalid student ID")
            elif choice == '2':
                student_id = input("Enter student ID: ")
                try :
                    print(f"\ncurrint courses : {students_data[student_id]["currint_courses"]}")
                except KeyError :
                    print("\n invalid inputs try again !")

            elif choice == '3':
                student_id = input("Enter student ID: ")
                try :
                    for i,course in enumerate(students_data[student_id]["currint_courses"]):
                        print(f"{i+1}. {course}")
                    selected_course = input("select courses to drop :").split()
                    drop_courses(students_data[student_id]["currint_courses"],selected_course)
                    save_change = True
                    print("\n The Course is Dropped Successfully")
                except KeyError :
                    print("\ninvalid student ID")


            elif choice == '4':
                save(students_data)
                print("\n All changes have been saved")
                save_change = False
            elif choice == '5':
                try:
                    if save_change == True:
                        ans = input("\n do you want to save changes press yes/no :")
                        if ans == "yes":
                            save(students_data)
                    save_change = False
                    break
                except NameError:
                    break

            else:
                print("\n Invalid choice. Please try again.")

    elif choice == '3':
        while True:
            print("\nManage Grades: ")
            print("1. Add Grades")
            print("2. List Grades of currint semester ")
            print("3. Save changes ")
            print("4. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                student_id = input("Enter student ID: ")
                try :
                    for i,course in enumerate(students_data[student_id]["currint_courses"]):

                        while True :
                            grade = input(f"{i + 1}. {course} = ")
                            try :
                                grade_ = float(grade)

                                while 0.0 > grade_ or grade_ > 100.0 :
                                    print("not valid grade !")
                                    grade_ = input(f"{i + 1}. {course} = ")
                                    grade_ = float(grade_)

                                x = add_grade(grade_,course,students_data[student_id]["semester_grades"],students_data[student_id]["pass_terms"],units_of_terms)
                                students_data[student_id]["Number_of_units"] += x
                                break
                            except ValueError :
                                print("grades except Numbers only ")
                                continue

                    students_data[student_id]["currint_courses"] = []
                    save_change = True

                except KeyError :
                    print("\ninvalid student ID")


            elif choice == '2':
                student_id = input("\nEnter student ID: ")
                try:
                    for term , grade in students_data[student_id]["semester_grades"].items():
                        if float(grade) >= 50.0 :
                            state = "Pass"
                        else :
                            state = "fail"
                        print(f"course : {term} -> {grade}  {state}")
                except KeyError :
                    print("\ninvalid student ID")

            elif choice == '3':
                save(students_data)
                print("\n All changes have been saved")
                save_change = False

            elif choice == '4':
                try:
                    if save_change == True:
                        ans = input("\n do you want to save changes press yes/no :")
                        if ans == "yes":
                            save(students_data)
                    save_change = False
                    break
                except NameError:
                    break

            else:
                print("Invalid choice. Please try again.")

    elif choice == '4':
        print("Session Termenated")
        break
