class Student:
    def __init__(self, name, surname, age, course):
        self.name = name
        self.surname = surname
        self.age = age
        self.course = course

    def get_info(self):
        return f"{self.name} {self.surname}, {self.age} лет, учится на курсе {self.course}"
