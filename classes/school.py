import csv
from classes.students import Student
from classes.staff import Staff

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_members()
        self.students = Student.all_members()

    def list_students(self):
        for idx, student in enumerate(self.students):
            print(f"{idx+1}. {student.name} {student.school_id}")
        
    def find_student_by_id(self, student_id):
        for stud in self.students:
            if student_id == stud.school_id:
                return stud
        print("this id does not match any students")
        return None
    def add_student(self,student_data):
        new_student = Student(**student_data)
        self.students.append(new_student)
