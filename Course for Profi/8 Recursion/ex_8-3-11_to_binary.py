'''
Функция to_binary()
Реализуйте функцию to_binary() с использованием рекурсии, которая принимает один аргумент:

number — неотрицательное целое число
Функция должна возвращать строковое представление числа number в двоичной системе счисления.

Примечание 1. Вспомнить алгоритм перевода числа из десятичной системы счисления в двоичную можно по ссылке.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами https://stepik.org/media/attachments/lesson/594137/tests_2429277.zip
GitHub https://github.com/python-generation/Professional/tree/main/Module_8/Module_8.3/Module_8.3.16
Sample Input 1:

print(to_binary(15))
Sample Output 1:

1111
Sample Input 2:

print(to_binary(0))
Sample Output 2:

0
Sample Input 3:

print(to_binary(1))
Sample Output 3:

1
'''


def to_binary(num_ten):
    if num_ten < 2:
        return num_ten
    else:
        return str(to_binary(num_ten // 2)) + str(num_ten % 2)


print(to_binary(15))
print(to_binary(123))
print(to_binary(0))
print(to_binary(1))