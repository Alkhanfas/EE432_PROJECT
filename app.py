from usage import *

print("""wellcome to our project here is a list of all commands :
1- add_students : to add student 
2- remove student : to remove all data of student 
3_ exit : to exit  
4_ 
5_
6_
""")

while True :
    comand = input("inter comand : ")

    if comand == "exit":
        break
    elif comand == "add student":
        student_name = input("enter student name : ")
        studentID = input("enter student_ID : ")
        add_student(student_name,studentID)
    elif comand == "remove student":
        studentID = input("enter studentID : ")
        delete_student(studentID)

