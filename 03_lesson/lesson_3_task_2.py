from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Samsung", "Galaxy S23", "+79158888888"))
catalog.append(Smartphone("Apple", "iPhone 14", "+79017777777"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 10", "+79231111111"))
catalog.append(Smartphone("Huawei", "P50 Pro", "+79348888888"))
catalog.append(Smartphone("OnePlus", "9 Pro", "+79457777777"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
