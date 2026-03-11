from student import Student

class CourseGroup:
    def __init__(self):
        self.student = None  # Основной студент
        self.classmates = []  # Список сокурсников

    def get_group_info(self):
        # Получаем информацию об основном студенте
        main_student_info = self.student.get_info()

        # Формируем список имён сокурсников
        classmates_names = [f"{s.name} {s.surname}" for s in self.classmates]
        classmates_str = ", ".join(classmates_names)

        return f"{main_student_info} вместе с: {classmates_str}"