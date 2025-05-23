'''
Функция print_operation_table()
Реализуйте функцию print_operation_table(), которая принимает три аргумента в следующем порядке:

operation — функция, характеризующая некоторую бинарную операцию
rows — натуральное число
cols — натуральное число
Функция должна составлять и выводить таблицу из rows строк и cols столбцов, в которой элемент со строкой n и столбцом
m имеет значение operation(n, m).

Примечание 1. Нумерация строк и столбцов в таблице начинается с единицы.

Примечание 2. Элементы в строках таблицы должны быть разделены одним пробелом, причем выравнивать таблицу
необязательно.

Примечание 3. Бинарная операция — математическая операция, принимающая два аргумента и возвращающая один результат.

Примечание 4. В тестирующую систему сдайте программу, содержащую только необходимую функцию print_operation_table(),
но не код, вызывающий ее.

Примечание 5. Тестовые данные доступны по ссылкам:

Архив с тестами https://stepik.org/media/attachments/lesson/640036/tests_2670420.zip
GitHub https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.3/Module_9.3.17
Sample Input 1:

print_operation_table(lambda a, b: a * b, 5, 5)
Sample Output 1:

1   2   3   4   5
2   4   6   8   10
3   6   9   12  15
4   8   12  16  20
5   10  15  20  25
Sample Input 2:

print_operation_table(pow, 5, 4)
Sample Output 2:

1   1   1   1
2   4   8   16
3   9   27  81
4   16  64  256
5   25  125 625
'''


def print_operation_table(operation, rows, col):
    matrix = [['_'] * col for _ in range(rows)]

    for n in range(len(matrix)):
        for m in range(len(matrix[n])):
            matrix[n][m] = operation(n + 1, m + 1)
        print(*matrix[n])


print_operation_table(pow, 5, 4)
print()
print_operation_table(lambda a, b: a * b, 5, 5)