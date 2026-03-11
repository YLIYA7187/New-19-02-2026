from address import Address
from mailing import Mailing

# Создаём адреса
from_addr = Address("150000", "Ярославль", "Угличская", "70", "2")
to_addr = Address("654321", "Санкт-Петербург", "Невский проспект", "45", "56")

mailing = Mailing(
    to_address=to_addr, from_address=from_addr, cost=500.0, track="TRACK123456789"
)

print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} -"
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)
