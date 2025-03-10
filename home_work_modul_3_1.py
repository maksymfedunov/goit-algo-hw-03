from datetime import datetime # импортируем модуль datetime 


def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date() # преобразовываем строку в datatime
        date_today = datetime.today().date()# получаем текущую дату
        difference = date_today - given_date # расчитываем разницу между датами
        return difference.days # возвращаем количество дней в формате целых чисел
    except ValueError:
        return "Invalid date format. Use YYYY-MM-DD format, please" # если введен неправильный формат, выводим сообщение об ошибке
            
    
