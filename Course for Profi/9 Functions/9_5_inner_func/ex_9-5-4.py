'''
Функция date_formatter()
Нередко в разных странах используются разные форматы дат. Рассмотрим часть из них:

код страны	формат даты
ru	DD.MM.YYYY
us	MM-DD-YYYY
ca	YYYY-MM-DD
br	DD/MM/YYYY
fr	DD.MM.YYYY
pt	DD-MM-YYYY
Реализуйте функцию date_formatter(), которая принимает один аргумент:

country_code — код страны
Функция date_formatter() должна возвращать функцию, которая принимает в качестве аргумента дату (тип date) и возвращает строку с данной датой в формате страны с кодом country_code.

Примечание 1. Гарантируется, что в функцию date_formatter() передаются только те коды стран, что перечислены в приведенной выше таблице.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию date_formatter(), но не код, вызывающий ее.
'''
from datetime import datetime, date


def date_formatter(country_code):
    formats = {'ru': '%d.%m.%Y',
               'us': '%m-%d-%Y',
               'ca': '%Y-%m-%d',
               'br': '%d/%m/%Y',
               'ft': '%d.%m.%Y',
               'pt': '%d-%m-%Y'}
    def inner(d):
        f = formats[country_code]
        return datetime.strftime(d, f)
    return inner


date_ru = date_formatter('us')
today = date(2025, 1, 5)
print(date_ru(today))