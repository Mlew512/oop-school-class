import csv

from classes.person import Person

class Staff(Person):
    def __init__(self, name, age, role, password,employee_id):
        super().__init__(name, age, role, password)
        self.employee_id = employee_id
    
    @classmethod
    def all_staff(cls):
        staff = []
        with open('./data/staff.csv', newline = '') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                new_staff = cls(**row)#assins data its key so its imputed correctly regardless of order
                staff.append(new_staff)
        # print(staff)
        return staff