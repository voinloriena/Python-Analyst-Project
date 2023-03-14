class Human:
    def __init__(self, name=None, familyname=None, age=None, gender=None, nationality=None):
        self.name = name
        self.familyname = familyname
        self.age = age
        self.gender = gender
        self.nationality = nationality

    def set_name(self,name=None):
        self.name=name

    def set_family(self,familyname=None):
        self.familyname=familyname

    def set_age(self,age=None):
        self.age=age

    def set_gender(self,gender=None):
        self.gender=gender

    def set_nationality(self,nationality=None):
        self.nationality=nationality

    def get_info(self):
        return vars(self)

class Student(Human):
    def __init__(self, name=None, familyname=None, age=None, gender=None, nationality=None, school=None, subject=[]):
        super().__init__(name = name, familyname=familyname, age=age, gender=gender, nationality=nationality)
        self.school=school
        self.subject=subject

    def set_school(self):
        return self.school

    def add_subject(self):
        self.subject.append(subject)

    def set_subject(self):
        return self.subject

class Teacher(Human):
    def __init__(self, name=None, familyname=None, age=None, gender=None, nationality=None, school=None, subject=None):
        super().__init__(name=name, familyname=familyname, age=age, gender=gender, nationality=nationality)
        self.school = school
        self.subject = subject

    def set_school(self):
        return self.school

    def add_subject(self, subject=None):
        self.subject=subject

    def set_subject(self):
        return self.subject
