from user import User

my_user = User(first_name="Алексей", last_name="Бельчук")

my_user.print_first_name()  # Выведет: Имя: Алексей
my_user.print_last_name()  # Выведет: Фамилия: Бельчук
my_user.print_full_name()  # Выведет: Полное имя: Алексей Бельчук
