# Вложенные классы
from Address import Address
from Mailing import Mailing

from_address = Address("1234567", "Москва", "Тверская", "10", "25")
to_address = Address("7654321", "Тольятти", "Луначарского", "20", "15")
Mailing1 = Mailing(to_address, from_address, 500, "RU123456789")

print(
    f"Отправление {Mailing1.track} "
    f"из {Mailing1.from_address.index}, {Mailing1.from_address.city}, "
    f"{Mailing1.from_address.street}, {Mailing1.from_address.house} - "
    f"{Mailing1.from_address.apartament} "
    f"в {Mailing1.to_address.index}, {Mailing1.to_address.city}, "
    f"{Mailing1.to_address.street}, {Mailing1.to_address.house} -"
    f"{Mailing1.to_address.apartament}. "
    f"Стоимость {Mailing1.cost} рублей."
)
