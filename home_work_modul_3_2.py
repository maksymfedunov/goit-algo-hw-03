import random


def get_numbers_ticket(min, max, quantity):
    try:
        if min >= 1 and max <= 1000 and 1 <= quantity <= (max - min +1): # задать диапазон для аргументов
            lottery_numbers = list(sorted(set(random.sample(range(min, max+1), quantity)))) # Сгенерировать отсортированный набор уникальных чисел
            print(lottery_numbers)
            return lottery_numbers
            
        else:                                
            print("Неверно введены данные")
            return []
    except TypeError: # Проверить правильность ввода
        print("Введите пожалуйста данные в цифрах") 
        return []        
        

