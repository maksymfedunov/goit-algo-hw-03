import re


def normalize_phone(phone_number):
    patter = r"[^0-9+]"#создаем паттерн
    
    number_clean = re.sub(patter, "", phone_number)#Оставляем в телефонном номере только цифры и "+"
    if not number_clean.startswith("+"):
        if number_clean.startswith("380"):
            number_clean = "+" + number_clean#добавляем "+", если номер не начинается с него или начинается с "380"
        else:
            number_clean = "+38" + number_clean#добавляем "+38", если номер начинается с "0"
    return number_clean      
            
    
        
        
   



   