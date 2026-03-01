def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    try:
        num = int(input("Введите число N: "))
        fizz_buzz(num)
    except ValueError:
        print("Ошибка: введите целое число!")
