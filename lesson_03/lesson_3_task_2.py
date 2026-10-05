# Список объектов
from smartphone import Smartphone


catalog = [
 Smartphone("Apple", "iPhone 15", "+7 900 111-22-33"),
 Smartphone("Samsung", "Galaxy S24", "+7 900 444-55-66"),
 Smartphone("Xiaomi", "Redmi Note 13", "+7 900 777-88-99"),
 Smartphone("Google", "Pixel 8", "+79444444444"),
 Smartphone("Huawei", "P60", "+79555555555")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
