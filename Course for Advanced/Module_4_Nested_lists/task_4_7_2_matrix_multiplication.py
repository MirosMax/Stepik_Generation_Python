'''
Умножение матриц 🌶️

Напишите программу, которая перемножает две матрицы.

Формат входных данных
На вход программе подаются два натуральных числа n и m — количество строк и столбцов в первой матрице, затем элементы
первой матрицы, затем пустая строка. Далее следуют числа m и k — количество строк и столбцов второй матрицы затем
элементы второй матрицы.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
'''


matrix_1 = []
matrix_2 = []

n, m = input().split()
n, m = int(n), int(m)

for i in range(n):
    row = [int(x) for x in input().split()]
    matrix_1.append(row)

space = input()
m, k = input().split()
m, k = int(m), int(k)

for i in range(m):
    row = [int(x) for x in input().split()]
    matrix_2.append(row)

result_matrix = []
for _ in range(n):
    row = [0 for _ in range(k)]
    result_matrix.append(row)

for i in range(k):
    for j in range(n):
        count = 0
        for k in range(m):
            count += matrix_1[i][k] * matrix_2[k][j]
        result_matrix[i][j] = count
        print(result_matrix[i][j], end=' ')
    print()

