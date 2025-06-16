'''
Функция filter_names()
Реализуйте генераторную функцию filter_names(), которая принимает три аргумента в следующем порядке:

names — список имен
ignore_char — одиночный символ
max_names — натуральное число
Функция должна возвращать генератор, порождающий max_names имён из списка names, игнорируя имена, которые

начинаются на ignore_char (в любом регистре)
содержат хотя бы одну цифру
Если max_names больше количества имен в списке names, то генератор должен породить все возможные имена из данного списка.

Примечание 1. Имена в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию filter_names(), но не код, вызывающий ее.
'''


def filter_names(names, ignore_char, max_names):
    filter_names = (
        name
        for name in names
        if not name.lower().startswith(ignore_char.lower()) and name.isalpha()
    )
    counter = 0
    for n in filter_names:
        counter += 1
        if counter > max_names:
            break
        yield n


data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 'D', 3))