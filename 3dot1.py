from datetime import datetime

def get_days_from_today(date_str):
    try:
        # Створюємо обьект datetime зі строки та перевіряємо корректність дати
        input_date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Ошибка: некорректная дата или формат")
        return None

    # розраховуємо кількість днів між датами
    today = datetime.today()
    delta = today - input_date
    return delta.days

# Приклади
print(get_days_from_today("2020-02-29"))  # Корерктна дата
print(get_days_from_today("2020-02-30"))  # Некоректна дата
print(get_days_from_today("2999-01-01"))  # Дата з майбутнього
    

        


