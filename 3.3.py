def normalize_phone(all_numbers):
    for i in range(len(all_numbers)):
        phone_number = all_numbers[i] 
        phone_number_list = [s for s in phone_number if s.isdigit()] 
        #створюємо з номеру телефона список, що включає в себе всі цифри номера

        if len(phone_number_list) < 10: #перевіряємо, чи є нуль на початку
            phone_number_list.insert(0, '0')
        if not (phone_number_list[0:2] == ['3', '8']): #перевіряемо, чи є код країни
            phone_number_list.insert(0, '8')
            phone_number_list.insert(0, '3')
        
        phone_number_list.insert(0, '+') #додаємо + у початок
        all_numbers[i] = ''.join(phone_number_list) #перетворюємо список назад у строку

    print(all_numbers)

raw_n = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
normalize_phone(raw_n)

        
        