'''
Функция dict_travel() 🌶️🌶️
Реализуйте функцию dict_travel(), которая принимает один аргумент:

nested_dicts — словарь, содержащий в качестве значений числа, строки или словари, которые, в свою очередь, так же
содержат в качестве значений числа, строки или словари; вложенность может быть произвольной
Функция должна выводить все пары ключ-значение словаря nested_dicts, а также значения всех его дочерних словарей.
При выводе значений дочерних словарей необходимо перечислять имена всех ключей, начиная с верхнего уровня, разделяя
их точками.

Например, в словаре:

{'name': 'Arthur', 'grades': {'math': 4, 'chemistry': 3}}
значение 4 должно быть выведено в следующем формате:

grades.math: 4
Все пары ключ-значение должны быть расположены в лексикографическом порядке, каждая на отдельной строке.

Примечание 1. Гарантируется, что ключами в подаваемом в функцию словаре являются строки, содержащие только латинские
буквы в нижнем регистре.

Примечание 2. Гарантируется, что ни один ключ в подаваемом в функцию словаре не является последовательностью других
ключей. Другими словами, словарь не может иметь, например, следующий вид:

{'b.c': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию dict_travel(), но не код,
вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами https://stepik.org/media/attachments/lesson/594680/tests_2646425.zip
GitHub https://github.com/python-generation/Professional/tree/main/Module_8/Module_8.4/Module_8.4.8
Sample Input 1:

data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}

dict_travel(data)
Sample Output 1:

a: 1
b.a: 10
b.b: 20
b.c: 30
Sample Input 2:

data = {'d': 1, 'b': {'c': 30, 'a': 10, 'b': 20}, 'a': 100}

dict_travel(data)
Sample Output 2:

a: 100
b.a: 10
b.b: 20
b.c: 30
d: 1
Sample Input 3:

data = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}

dict_travel(data)
Sample Output 3:

b.a: 10
b.b.d: 40
b.b.e: 50
b.c: 30
'''

# # 1 вариант
# def dict_travel(nested_dicts):
#     def rec(nested_dicts, path=None):
#         if path is None:
#             path = []
#         for k, v in sorted(nested_dicts.items(), key=lambda i: (i[0], i[1])):
#             if isinstance(v, dict):
#                 rec(v, path + [k])
#             else:
#                 print(f'{".".join(path + [k])}: {v}')
#
#     rec(nested_dicts)


# 2 вариант, оптимальнее
def dict_travel(nested_dicts):
    for k, v in sorted(nested_dicts.items()):
        if isinstance(v, dict):
            new_dict = {f'{k}.{k_in}': v_in for k_in, v_in in v.items()}
            dict_travel(new_dict)
        else:
            print(f'{k}: {v}')


# INPUT DATA:

# TEST_1:
data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}

dict_travel(data)

# TEST_2:
data = {'d': 1, 'b': {'c': 30, 'a': 10, 'b': 20}, 'a': 100}

dict_travel(data)

# TEST_3:
data = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}

dict_travel(data)
#
# # TEST_4:
# data = {'firstname': 'Alyson', 'lastname': 'Hannigan', 'birthday': {'day': 24, 'month': 'March', 'year': 1974}}
#
# dict_travel(data)
#
# # TEST_5:
# data = {'firstname': 'Тимур', 'lastname': 'Гуев', 'birthdate': {'day': 10, 'month': 'October', 'year': 1993},'address': {'streetaddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область', 'type': 'город', 'cityname': 'Москва'}, 'postalcode': '125315'}}
#
# dict_travel(data)