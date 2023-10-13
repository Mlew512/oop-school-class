# from classes.staff import Staff
# from classes.students import Student
from classes.school import School

school = School("Ridgemont High")

# print(school.name)
# print(school.staff)

# print(school.students)


while True:
    mode = input(
        "\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student\n3. Add a Student\n4. Remove a Student\n5. Quit\n"
    )

    if mode == "1":
        school.list_students()
    elif mode == "2":
        student_id = input("input the student id sir or madamn: ")
        student_string = str(school.find_student_by_id(student_id))
        print(student_string)
    elif mode == "3":
        student_data = {"role": "student"}
        student_data["name"] = input("Enter student name:\n")
        student_data["age"] = input("Enter student age: \n")
        student_data["school_id"] = input("Enter student school id: \n")
        student_data["password"] = input("Enter student password: \n")
        school.add_student(student_data)
    elif mode == "4":
        student_id = input("input the student id sir or madamn: ")
        student_string = school.find_student_by_id(student_id)
        if student_string:
            school.students.remove(student_string)
            print("student expelled!")
            
    elif mode == "5":
        print("bye bye bye bye bye")
        break
    else:
        pass
