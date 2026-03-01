def month_to_season(month_number):
    seasons = {
        1: "Зима",
        2: "Зима",
        3: "Весна",
        4: "Весна",
        5: "Весна",
        6: "Лето",
        7: "Лето",
        8: "Лето",
        9: "Осень",
        10: "Осень",
        11: "Осень",
        12: "Зима",
    }

    return seasons.get(month_number, "Нет такого месяца")


# Пример использования:
number = int(input("Введите номер месяца (1-12): "))
season = month_to_season(number)
print(f"{number}-й месяц — это {season}.")
