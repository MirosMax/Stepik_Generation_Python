'''
Напишите программу, которая перемножает две матрицы.

Формат входных данных
На вход программе подаются два натуральных числа n и m — количество строк и столбцов в первой матрице, затем элементы
первой матрицы, затем пустая строка. Далее следуют числа m и k — количество строк и столбцов второй матрицы затем
элементы второй матрицы.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
'''

n, m = input().split()
n, m = int(n), int(m)

matrix_1 = []
matrix_2 = []

for i in range(n + n + 1):
    s = input()
    if i == n:
        continue
    elif i < n:
        row = [int(x) for x in s.split()]
        matrix_1.append(row)
    else:
        row = [int(x) for x in s.split()]
        matrix_2.append(row)

result_matrix = []
for _ in range(n):
    row = [0 for _ in range(m)]
    result_matrix.append(row)

for i in range(n):
    for j in range(m):
        result_matrix[i][j] = matrix_1[i][j] + matrix_2[i][j]
        print(result_matrix[i][j], end=' ')
    print()
