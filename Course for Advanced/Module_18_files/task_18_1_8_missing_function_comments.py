'''
Пропущенные комменты 🌶️

При написании собственных функций рекомендуется в комментарии описывать назначение функции, ее параметры и возвращаемое
значение. Часто программисты откладывают написание таких комментариев напоследок, а потом и вовсе забывают о них 😂.

На вход программе подается строка текста с именем текстового файла, в котором написан код на языке Python. Напишите
программу, выводящую на экран имена всех функций, для которых отсутствует поясняющий комментарий. Будем считать, что
любая строка, начинающаяся со слова def и пробела, является началом определения функции. Функция содержит комментарий,
если первый символ предыдущей строки - #.

Формат входных данных
На вход программе подается строка текста, содержащая имя существующего текстового файла с кодом на языке Python.

Формат выходных данных
Программа должна вывести названия всех функций (не меняя порядка их следования в исходном файле), каждое на отдельной
строке, для которых отсутствует поясняющий комментарий. Если все функции в файле имеют поясняющий комментарий, то
следует вывести: Best Programming Team.

Примечание 1. Если бы файл содержал код:

def powers(a):
    return a, a**2, a**3

# функция вычисляет сумму всех переданных чисел
def sum_all(*args):
    return sum(args)

def matrix():
    pass

# функция возвращает количество переданных аргументов
def count_args(*args):
    return len(args)

def mean(*args):
    total = 0.0
    count = 0
    for i in args:
        if type(i) in (int, float):
            total += i
            count += 1
    if count == 0:
        return 0.0
    else:
        return total / count

def greet(name, *args):
    args = (name,) + args
    return f'Hello, {" and ".join(args)}!'

# функция вычисляет факториал переданного числа
def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

то результатом будет:

powers
matrix
mean
greet

Примечание 2. Гарантируется, что в файле есть хотя бы одна функция при этом вложенных функций в файле нет.
'''

with open('comment_func.txt', 'r', encoding='utf-8') as input_file:
    list_func = [s for s in input_file.read().split('\n') if s.startswith('def ') or s.startswith('#')]
    miss_comment = []
    for i in range(len(list_func)):
        if 'def ' in list_func[i]:
            name_func = list_func[i][4:list_func[i].find('(')]
            if i == 0 or '#' not in list_func[i - 1]:
                miss_comment.append(name_func)
    if miss_comment:
        print(*miss_comment, sep='\n')
    else:
        print('Best Programming Team')
