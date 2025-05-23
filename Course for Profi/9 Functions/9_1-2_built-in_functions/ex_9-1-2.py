'''
Функция convert()
Реализуйте функцию convert(), которая принимает один аргумент:

number — целое число
Функция должна возвращать кортеж из трех элементов, расположенных в следующем порядке:

двоичное представление числа number в виде строки без префикса 0b
восьмеричное представление числа number в виде строки без префикса 0o
шестнадцатеричное представление числа number в виде строки в верхнем регистре без префикса 0x
Примечание 1. В задаче удобно воспользоваться функциями bin(), oct() и hex().

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию convert(), но не код,
вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами https://stepik.org/media/attachments/lesson/640035/tests_2659185.zip
GitHub https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.1/Module_9.1.5
Sample Input 1:

print(convert(15))
Sample Output 1:

('1111', '17', 'F')
Sample Input 2:

print(convert(-24))
Sample Output 2:

('-11000', '-30', '-18')
Sample Input 3:

print(convert(1))
Sample Output 3:

('1', '1', '1')
'''


def convert(num):
    sign = ''
    if num < 0:
        sign = '-'
    res = [bin(num), oct(num), hex(num).upper()]
    return tuple(map(lambda a: sign + a.split('0', 1)[1][1:], res))


print(convert(15))
print(convert(-24))