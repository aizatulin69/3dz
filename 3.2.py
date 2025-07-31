from datetime import datetime
import time

def get_numbers_ticket(min_v, max_v, quantity):
    lottery_numbers = []
    
    if min_v<1 or max_v>1000: #перевіряемо вводні дані
        print("Enter another numder")
    else:
        while len(lottery_numbers) < quantity: 
                random_num = datetime.now().microsecond % (max_v - min_v) + min_v #обчислюємо випадкове число
                i=-1
                i=i+1
                lottery_numbers.append(random_num)
                time.sleep(float(str("0.0" + str(lottery_numbers[i])))) 
                #створюємо невеличку затримку випадкової довжини в виконанні коду, щоб наступне випадкове значення відрізнялось від попереднього
    print(lottery_numbers)
    return lottery_numbers
    
get_numbers_ticket(1, 100, 10)