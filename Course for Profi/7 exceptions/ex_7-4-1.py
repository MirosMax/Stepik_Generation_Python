'''
Функция get_weekday()
Реализуйте функцию get_weekday(), которая принимает один аргумент:

number — целое число (от 1 до 7 включительно)
Функция должна возвращать полное название дня недели на русском, который соответствует числу number, при этом:

если number не является целым числом, функция должна возбуждать исключение:
TypeError('Аргумент не является целым числом')
если number является целым числом, но не принадлежит отрезку [1;7], функция должна возбуждать исключение:
ValueError('Аргумент не принадлежит требуемому диапазону')

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_weekday(),
но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами https://stepik.org/media/attachments/lesson/640051/tests_2713716.zip
GitHub https://github.com/python-generation/Professional/tree/main/Module_7/Module_7.4/Module_7.4.18
Sample Input 1:

print(get_weekday(1))
Sample Output 1:

Понедельник
Sample Input 2:

try:
    print(get_weekday('hello'))
except Exception as err:
    print(err)
    print(type(err))
Sample Output 2:

Аргумент не является целым числом
<class 'TypeError'>
Sample Input 3:

try:
    print(get_weekday(8))
except ValueError as err:
    print(err)
    print(type(err))
Sample Output 3:

Аргумент не принадлежит требуемому диапазону
<class 'ValueError'>
'''


def get_weekday(num):
    import calendar
    import locale

    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    names = calendar.day_name

    try:
        day = names[num - 1]
        if num < 1 or num > 7:
            raise ValueError('Аргумент не принадлежит требуемому диапазону')
        return day.capitalize()
    except TypeError:
        raise TypeError('Аргумент не является целым числом')
    except IndexError:
        raise ValueError('Аргумент не принадлежит требуемому диапазону')


# INPUT DATA:

# TEST_1:
print(get_weekday(1))

# TEST_2:
try:
    print(get_weekday('hello'))
except Exception as err:
    print(err)
    print(type(err))

# TEST_3:
try:
    print(get_weekday(8))
except ValueError as err:
    print(err)
    print(type(err))

# TEST_4:
try:
    print(get_weekday(7))
except Exception as err:
    print(err)
    print(type(err))
else:
    print('Без ошибок')

# TEST_5:
print(get_weekday(2))

# TEST_6:
print(get_weekday(3))

# TEST_7:
print(get_weekday(4))

# TEST_8:
print(get_weekday(5))

# TEST_9:
print(get_weekday(6))

# TEST_10:
print(get_weekday(7))

# TEST_11:
try:
    print(get_weekday(4.0))
except Exception as err:
    print(err)
    print(type(err))

# TEST_12:
try:
    print(get_weekday('4'))
except Exception as err:
    print(err)
    print(type(err))

# TEST_13:
try:
    print(get_weekday(0))
except ValueError as err:
    print(err)
    print(type(err))

# TEST_14:
try:
    print(get_weekday(-5))
except ValueError as err:
    print(err)
    print(type(err))

# TEST_15:
try:
    print(get_weekday([]))
except Exception as err:
    print(err)
    print(type(err))

# TEST_16:
try:
    print(get_weekday((1, 2)))
except Exception as err:
    print(err)
    print(type(err))

# TEST_17:
try:
    print(get_weekday({}))
except Exception as err:
    print(err)
    print(type(err))

# TEST_18:
try:
    print(get_weekday(set()))
except Exception as err:
    print(err)
    print(type(err))