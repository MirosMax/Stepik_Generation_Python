'''
Возведение матрицы в степень 🌶️

Напишите программу, которая возводит квадратную матрицу в m-ую степень.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы,
затем натуральное число m.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
'''
import copy


def exp_matrix(matrix, matrix_2, n):
    temp_matrix = []
    for _ in range(n):
        row = [0 for _ in range(n)]
        temp_matrix.append(row)

    for i in range(n):
        for j in range(n):
            count = 0
            for k in range(n):
                count += matrix[i][k] * matrix_2[k][j]
            temp_matrix[i][j] = count

    return temp_matrix


n = int(input())

matrix = []
for i in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

m = int(input())

matrix_2 = copy.deepcopy(matrix)

for _ in range(m - 1):
    matrix_2 = exp_matrix(matrix, matrix_2, n)


for i in range(n):
    for j in range(n):
        print(matrix_2[i][j], end=' ')
    print()

