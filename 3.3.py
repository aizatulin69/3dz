def normalize_phone(phone_number):
    # Створюємо список лише з цифр, ігноруючи всі символи (пробіли, дужки, плюси тощо)
    phone_number_list = [s for s in phone_number if s.isdigit()]

    # Якщо номер коротший за 10 цифр — додаємо 0 на початок (наприклад, було 501234567)
    if len(phone_number_list) < 10:
        phone_number_list.insert(0, '0')

    # Якщо номер не починається з коду країни '38' — додаємо '38' на початок
    if not (phone_number_list[0:2] == ['3', '8']):
        phone_number_list.insert(0, '8')
        phone_number_list.insert(0, '3')

    # Додаємо '+' перед кодом країни
    phone_number_list.insert(0, '+')

    # Перетворюємо список назад у рядок і повертаємо результат
    return ''.join(phone_number_list)

print(normalize_phone("050-123-45-67"))
        
