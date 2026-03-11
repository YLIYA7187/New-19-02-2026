class Smartphone:
    def __init__(self, brand, model, phone_number):
        self.brand = brand  # марка телефона
        self.model = model  # модель телефона
        self.phone_number = phone_number  # абонентский номер


my_phone = Smartphone("Samsung", "Galaxy S24", "+79159827187")

# Вывод значений атрибутов объекта
print(f"Марка: {my_phone.brand}")
print(f"Модель: {my_phone.model}")
print(f"Абонентский номер: {my_phone.phone_number}")
