from datetime import datetime
import time

def get_numbers_ticket(min_v, max_v, quantity):
    lottery_numbers = []
    max_v += 1

    if min_v<1 or max_v>1000: #перевіряемо вводні дані
        print("numbers must be between 1 and 1000")
    elif min_v>=max_v:
        print("The min number must be less than the max number.")
    elif (max_v - min_v) < quantity:
        print("quantity must be less than the difference between the min and max numbers")
    else:
        while len(lottery_numbers) < quantity: 
                random_num = datetime.now().microsecond % (max_v - min_v) + min_v #обчислюємо випадкове число
                i=-1
                i=i+1
                is_repeat = False
                for o in range (len(lottery_numbers)): #перевіряємо, чи є число унікальним
                    if random_num == lottery_numbers[o]:
                        is_repeat = True

                if is_repeat == False: # якщо число унікальне, поповнюємо список
                    lottery_numbers.append(random_num)

                time.sleep(0.001 * (random_num % 100)) 
                #створюємо невеличку затримку випадкової довжини в виконанні коду, щоб наступне випадкове значення відрізнялось від попереднього
    print(lottery_numbers)
    return lottery_numbers
    
get_numbers_ticket(10, 100, 90)
