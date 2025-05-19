'''
Функция linear()
Линеаризация — это процесс преобразования списка, который может содержать несколько уровней вложенных списков, в
список, содержащий все те же элементы без какой-либо вложенности.

Например, список:

[1, [2, 3], [4, [5, 6, [7, 8, 9]]]]
после линеаризации будет иметь вид:

[1, 2, 3, 4, 5, 6, 7, 8, 9]
Реализуйте linear() с использованием рекурсии, которая принимает один аргумент:

nested_lists — список, элементами которого являются целые числа или списки, элементами которых, в свою очередь,
также являются либо целые числа, либо списки; вложенность может быть произвольной
Функция должна возвращать новый список, представляющий собой линеаризованный список nested_lists.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию linear(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами https://stepik.org/media/attachments/lesson/594680/tests_2429560.zip
GitHub https://github.com/python-generation/Professional/tree/main/Module_8/Module_8.4/Module_8.4.5
Sample Input 1:

my_list = [3, [4], [5, [6, [7, 8]]]]

print(linear(my_list))
Sample Output 1:

[3, 4, 5, 6, 7, 8]
Sample Input 2:

my_list = [10, 20, 30, 40, 50]

print(linear(my_list))
Sample Output 2:

[10, 20, 30, 40, 50]
'''


def linear(nested_lists):
    result = []
    for i in nested_lists:
        if isinstance(i, int):
            result.append(i)
        else:
            result.extend(linear(i))
    return result


# INPUT DATA:

# TEST_1:
my_list = [3, [4], [5, [6, [7, 8]]]]

print(linear(my_list))

# TEST_2:
my_list = [10, 20, 30, 40, 50]

print(linear(my_list))

# TEST_3:
my_list = [[1], [2], [3], [4, 5], 6, 7]

print(linear(my_list))

# TEST_4:
my_list = [[123], 23, 43, 65, 754, 3, 1, 2]

print(linear(my_list))

# TEST_5:
my_list = [3123, 424, 5343, 11, 1, 23, 43, 65, 754, 3, 1, [2]]

print(linear(my_list))

# TEST_6:
my_list = [[3, 2, 5345, 65, 7, 777, 0, 43, 65, 754, 3, 1, 2]]

print(linear(my_list))

# TEST_7:
my_list = [34534, [656, [7867, [[234, [123, 34534, [758, 978]]]], 667, [4546]]], [2324, [234234, [7656]], 9879, 55]]

print(linear(my_list))

# TEST_8:
my_list = [12, [13, [53, [632, [6, [2342341, [98, [3123], [2432], [4324]]]]]]]]

print(linear(my_list))

# TEST_9:
my_list = [3, [4], [5, [6, [7, 8]]]]
print(linear(my_list))

my_list = [3, [4], [5, [6, [7, 8]]]]
print(linear(my_list))