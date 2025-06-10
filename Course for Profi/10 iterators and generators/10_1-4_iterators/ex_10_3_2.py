'''
Функция is_iterable()
Реализуйте функцию is_iterable(), которая принимает один аргумент:

obj — произвольный объект
Функция должна возвращать True, если объект obj является итерируемым объектом, или False в противном случае.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_iterable(), но не код, вызывающий ее.
'''
def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False


# INPUT DATA:

# TEST_1:
print(is_iterable(18731))

# TEST_2:
print(is_iterable('18731'))

# TEST_3:
objects = [(1, 13), 7.0004, [1, 2, 3]]

for obj in objects:
    print(is_iterable(obj))

# TEST_4:
for element in [34, [4, 5], (4, 5), {"a":4}, "dfsdf", 4.5]:
    print(element, 'iterable: ', is_iterable(element))