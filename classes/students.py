import csv

from classes.person import Person 

class Student(Person):
    def __init__(self, name, age, role, password,school_id):
        super().__init__(name, age, role, password)
        self.school_id= school_id

    @classmethod
    def all_students(cls):
        students = []
        with open('./data/students.csv', newline = '') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                #name, age, role, student_id, password
                new_student = cls(**row)
                students.append(new_student)
        # print(students)
        return students
    
    def __str__(self):
        return f"""
        {self.name}
        ---------------
        age:{self.age}
        id:{self.school_id}\
        """