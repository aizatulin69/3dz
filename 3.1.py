from datetime import datetime 

def get_days_from_today(date_tuple):
    try: # Пробуємо створити об'єкт дати з кортежу (рік, місяць, день)
        input_date = datetime(*date_tuple)
    except ValueError:
        print("Помилка: некоректна дата")
        return None

    today = datetime.today()

    if input_date > today: 
        print("Помилка: дата з майбутнього")
        return None

    # Обчислюємо різницю між сьогоднішньою датою та введеною
    delta = today - input_date

    return delta.days

print(get_days_from_today((2020, 2, 29)))  # Коректна дата
print(get_days_from_today((2020, 2, 30)))  # Некоректна дата
print(get_days_from_today((2999, 1, 1)))   # Дата з майбутнього
    

        

