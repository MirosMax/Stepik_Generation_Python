'''
Коллекции
Напишите программу, которая принимает на вход корректный непустой список, корректный непустой кортеж или корректное
множество произвольной длины, и выполняет следующее:

если введен список, выводит его последний элемент
если введен кортеж, выводит его первый элемент
если введено множество, выводит количество его элементов
Формат входных данных
На вход программе подается корректный непустой список, кортеж или корректное произвольной длины множество.

Формат выходных данных
Программа должна вывести определенное значение, в зависимости от типа введенной коллекции.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами https://stepik.org/media/attachments/lesson/645394/tests_2666220.zip
GitHub https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.2/Module_9.2.20
Sample Input 1:

[[1, 2], [3, 4], [5, 6]]
Sample Output 1:

[5, 6]
Sample Input 2:

{'Arthur', 'Timur', 'Anri', 'Ruslan', 'Dima'}
Sample Output 2:

5
Sample Input 3:

('black', 'blue', 'red', 'orange', 'green', 'gray')
Sample Output 3:

black
'''

data = eval(input())
#
# if isinstance(data, list):
#     print(data[-1])
# elif isinstance(data, tuple):
#     print(data[0])
# elif isinstance(data, set):
#     print(len(data))


# 2 вариант, оптимальный
variants = {
    list: 'data[-1]',
    tuple: 'data[0]',
    set: 'len(data)'
}
print(eval(variants[type(data)]))

