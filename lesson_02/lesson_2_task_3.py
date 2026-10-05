# Площадь квадрата
# Добавлен комментарий в файл_3
from math import ceil


def square(side):
    area = side * side
    return (area)


# Здесь .replace()просто заменяет запятую на точку перед преоб-ем в число
side = ceil(float(input("Введите размер стороны: ").replace(",", ".")))
result = square(side)
print(f"Площадь квадрата: {result}")
