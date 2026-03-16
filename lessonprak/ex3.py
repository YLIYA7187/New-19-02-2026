from student import Student
from course_group import CourseGroup

# Создаём основного студента
main_student = Student("Иван", "Петров", 20, 3)

# Создаём сокурсников
classmate1 = Student("Мария", "Сидорова", 19, 3)
classmate2 = Student("Алексей", "Иванов", 21, 3)
classmate3 = Student("Елена", "Козлова", 20, 3)

# Создаём экземпляр класса CourseGroup
group = CourseGroup()

# Заполняем поля класса
group.student = main_student
group.classmates = [classmate1, classmate2, classmate3]

# Распечатываем информацию о группе
print(group.get_group_info())
