'''
Функция is_available_date() 🌶️
Во время визита очередного гостя сотрудникам отеля приходится проверять, доступна ли та или иная дата для бронирования
номера.

Реализуйте функцию is_available_date(), которая принимает два аргумента в следующем порядке:

booked_dates — список строковых дат, недоступных для бронирования. Элементом списка является либо одиночная дата, либо
период (две даты через дефис). Например:
['04.11.2021', '05.11.2021-09.11.2021']
date_for_booking — одиночная строковая дата или период (две даты через дефис), на которую гость желает забронировать
номер. Например:
'01.11.2021' или '01.11.2021-04.11.2021'
Функция is_available_date() должна возвращать True, если дата или период date_for_booking полностью доступна для
бронирования. В противном случае функция должна возвращать False.

Примечание 1. Гарантируется, что в периоде левая дата всегда меньше правой.

Примечание 2. В периоде (две даты через дефис) граничные даты включены.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_available_date(), но не
код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами https://stepik.org/media/attachments/lesson/611754/tests_2506745.zip
GitHub https://github.com/python-generation/Professional/tree/main/Module_3/Module_3.3/Module_3.3.19
'''
from datetime import datetime, date


def period_of_dates(dates: str):
    # возвращает список дней начиная с 0001-01-01
    f = '%d.%m.%Y'
    result = []
    if '-' in dates:
        temp = dates.split('-')
        start = datetime.strptime(temp[0], f).toordinal()
        stop = datetime.strptime(temp[1], f).toordinal()
        for d in range(start, stop + 1):
            result.append(d)
    else:
        result.append(datetime.strptime(dates, f).toordinal())
    return result


def is_available_date(booked_dates, date_for_booking):
    days_for_booking = period_of_dates(date_for_booking)
    booked_days = []
    for i in range(len(booked_dates)):
        booked_days += period_of_dates(booked_dates[i])
    for day in days_for_booking:
        if day in booked_days:
            return False
    return True