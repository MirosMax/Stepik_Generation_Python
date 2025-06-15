'''
Функция cubes_of_odds()
Вам доступна генераторная функция cubes_of_odds(), принимающая в качестве аргумента итерируемый объект, элементами которого являются целые числа, и возвращающая генератор, порождающий последовательность нечетных чисел переданного итерируемого объекта, возведенных в третью степень.

Перепишите данную функцию с использованием генераторного выражения, чтобы она выполняла ту же задачу.

Примечание 1. Если генераторное выражение становится достаточно большим, его можно записать в виде нескольких строк.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию cubes_of_odds(), но не код, вызывающий ее.
'''

# исходный вариант
# def cubes_of_odds(iterable):
#     for number in iterable:
#         if number % 2:
#             yield number ** 3


def cubes_of_odds(iterable):
    yield from (
        i ** 3
        for i in iterable
        if i % 2
    )


# INPUT DATA:

# TEST_1:
print(*cubes_of_odds([1, 2, 3, 4, 5]))

# TEST_2:
evens = [2, 4, 6, 8, 10]

print(list(cubes_of_odds(evens)))

# TEST_3:
data = tuple(range(432, 3845, 17))

print(*cubes_of_odds(data))

# TEST_4:
data = map(abs, range(-200, 400, 11))

print(*cubes_of_odds(data))

# TEST_5:
data = filter(lambda x: x % 13, range(101, 982))

print(*cubes_of_odds(data))