'''
Функция recursive_sum()
Реализуйте recursive_sum() с использованием рекурсии, которая принимает один аргумент:

nested_lists — список, элементами которого являются целые числа или списки, элементами которых, в свою очередь,
также являются либо целые числа, либо списки; вложенность может быть произвольной
Функция должна вычислять сумму всех чисел во всех списках и возвращать полученный результат. Если список
nested_lists пуст, функция должна вернуть число 0.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию recursive_sum(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами https://stepik.org/media/attachments/lesson/594680/tests_2429555.zip
GitHub https://github.com/python-generation/Professional/tree/main/Module_8/Module_8.4/Module_8.4.4
Sample Input 1:

my_list = [1, [4, 4], 2, [1, [2, 10]]]

print(recursive_sum(my_list))
Sample Output 1:

24
Sample Input 2:

my_list = []

print(recursive_sum(my_list))
Sample Output 2:

0
'''


def recursive_sum(nested_lists):
    if isinstance(nested_lists, int):
        return nested_lists
    if isinstance(nested_lists, list):
        if not nested_lists:
            return 0
        return recursive_sum(nested_lists[0]) + recursive_sum(nested_lists[1:])


my_list = []

print(recursive_sum(my_list))

