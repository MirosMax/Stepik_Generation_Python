'''
Функция get_min_max() 😳
Реализуйте функцию get_min_max(), которая принимает один аргумент:

iterable — итерируемый объект, элементы которого сравнимы между собой
Функция должна возвращать кортеж, в котором первым элементом является минимальный элемент итерируемого объекта iterable, вторым — максимальный элемент итерируемого объекта iterable. Если итерируемый объект iterable пуст, функция должна вернуть значение None.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_min_max(), но не код, вызывающий ее.
'''


def get_min_max(iterable):
    min_el = None
    max_el = None
    for i in iterable:
        if min_el is None:
            min_el = i
        elif i < min_el:
            min_el = i
        if max_el is None:
            max_el = i
        elif i > max_el:
            max_el = i
    if not min_el is None:
        return min_el, max_el
    return None
