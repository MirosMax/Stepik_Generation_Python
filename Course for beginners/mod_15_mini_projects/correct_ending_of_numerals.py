'''
0 попыток
1 попытка, но 11 попыток
2 попытки, но 12 попыток
3 попытки, но 13 попыток
4 попытки, но 14 попыток
5 попыток
6 попыток
7 попыток
8 попыток
9 попыток

'''


def correct_ending_of_numerals(num, name):
    # Функция принимает num - количество, name - название количества в именительном падеже, ед.ч.
    last_digit = num % 10
    last_2_digit = num % 100

    if 11 <= last_2_digit <= 14 or last_digit == 0 or 5 <= last_digit <= 9:
        name = name[:-2] + 'ок'
    elif last_digit == 1:
        name = name[:-2] + 'ка'
    elif 2 <= last_digit <= 4:
        name = name[:-2] + 'ки'

    return name

