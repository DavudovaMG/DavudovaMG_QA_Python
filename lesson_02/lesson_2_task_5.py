# Месяц — сезон
def month_to_season(month):
    if (1 < month < 2) or (month == 12):
        return "зима"
    if 3 <= month <= 5:
        return "весна"
    if 6 <= month <= 8:
        return "лето"
    if 9 <= month <= 11:
        return "осень"
    return "Неверный номер месяца"


month = int(input("Введите номер месяца (1-12): "))
print(month_to_season(month))
