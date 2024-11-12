'''
Задача Иосифа Флавия 🌶️🌶️
n человек, пронумерованных числами от 1 до n, стоят в кругу. Они начинают считаться, каждый k-й по счету человек
выбывает из круга, после чего счет продолжается со следующего за ним человека. Напишите программу, определяющую
номер человека, который останется в кругу последним.

Формат входных данных
На вход программе подаются два числа
n и k, записанные на отдельных строках.

Формат выходных данных
Программа должна вывести одно число – номер человека, который останется в кругу последним.

Примечание 1. Подробнее ознакомиться с классической задачей Иосифа Флавия можно по ссылке
https://ru.wikipedia.org/wiki/Задача_Иосифа_Флавия

Примечание 2. Визуализацию работы алгоритма можно посмотреть по ссылке https://www.geogebra.org/m/ExvvrBbR
'''

num_of_people = int(input('Введите количество человек: '))
k = int(input('Задайте позицию k: '))

range_num = [i for i in range(1, num_of_people + 1)]
start = 0
print(range_num)

while len(range_num) > 1:
    del_position = start + k - 1
    if 0 <= del_position <= len(range_num) - 1:
        del range_num[del_position]
    else:
        while not 0 <= del_position <= len(range_num) - 1:
            del_position -= len(range_num)
        del range_num[del_position]
    if 0 <= del_position <= len(range_num) - 1:
        start = del_position
    else:
        start = del_position - len(range_num)
    print(range_num)

print('Ответ:', *range_num)


