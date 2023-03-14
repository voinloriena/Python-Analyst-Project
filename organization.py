import csv
from users import Student,Teacher
class School:
    def __init__(self, name=None, address=None, phone=None, email=None, num_stud=None, num_teachers=None):
        self.name = name
        self.address=address
        self.phone=phone
        self.email=email
        self.num_stud=num_stud
        self.num_teachers=num_teachers
        self.teachers=[]
        self.students=[]

    def add_teacher(self, teacher):
        if teacher not in self.teachers:
            self.teachers.append(teacher)
            self.set_num_teachers(len(self.teachers))

    def set_student(self, student):
        if student not in self.students:
            self.students.append(student)
            self.set_num_stud(len(self.students))

    def set_name(self):
        return self.name

    def set_address(self):
        return self.address

    def set_phone(self):
        return self.phone

    def set_email(self):
        return self.email

    def set_num_stud(self, count):
        self.num_stud = count

    def set_num_teachers(self, count):
        self.num_stud = count

    def set_num_teachers(self, count):
        self.num_teachers = count

    def get_info(self):
        return vars(self)

    def get_report(self):
        with open('report.csv', 'w') as f:
            [f.write('{0}:{1}\n'.format(key,value)) for key, value in vars(self).items()]




