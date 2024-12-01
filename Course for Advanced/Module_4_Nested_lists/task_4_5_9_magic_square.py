'''
Магический квадрат 🌶️
Магическим квадратом порядка n называется квадратная таблица размера n×n, составленная из всех чисел 1, 2, 3, …, n**2
так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу,
которая проверяет, является ли заданная квадратная матрица магическим квадратом.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы:
n строк, по n чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести YES, если матрица является магическим квадратом, или NO в противном случае.
'''


n = int(input())

matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

verification_amount = sum(matrix[0])

flag = 'YES'

# проверка наличия всех чисел в матрице от 1 до n**2
ver_list_num = [i for i in range(1, n ** 2 + 1)]
temp = []
for i in range(n):
    for j in range(n):
        temp.append(matrix[i][j])
for i in ver_list_num:
    if i not in temp:
        flag = 'NO'
        break

# проверка строк
if flag == 'YES':
    for i in range(1, n):
        if sum(matrix[i]) != verification_amount:
            flag = 'NO'
            break

# переворачиваем матрицу и проверяем столбцы
if flag == 'YES':
    rotated_matrix = []
    for i in range(n):
        temp = []
        for j in range(-1, -(n + 1), -1):
            temp.append(matrix[j][i])
        rotated_matrix.append(temp)
    for i in range(n):
        if sum(rotated_matrix[i]) != verification_amount:
            flag = 'NO'
            break

# проверяем диагонали
if flag == 'YES':
    counter_main = 0
    counter_secondary = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                counter_main += matrix[i][j]
            if i + j + 1 == n or j == n - i - 1:
                counter_secondary += matrix[i][j]
    if counter_main != verification_amount or counter_secondary != verification_amount:
        flag = 'NO'

print(flag)