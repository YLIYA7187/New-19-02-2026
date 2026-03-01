import math


def square(side_length):
    result = side_length**2
    if not isinstance(side_length, int):
        result = math.ceil(result)
    return result


side = float(input("Введите длину стороны квадрата: "))
area = square(side)
print(f"Площадь квадрата со стороной {side} равна {area}.")
