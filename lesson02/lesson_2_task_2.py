def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


# year_to_check = 2024

# result = is_year_leap(year_to_check)

# print(f"год {year_to_check}: {result}")

year_input = int(input("Введите год: "))

result = is_year_leap(year_input)

print(f"год {year_input}: {result}")
