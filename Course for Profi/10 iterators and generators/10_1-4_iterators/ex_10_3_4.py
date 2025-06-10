'''
Функция random_numbers()
Реализуйте функцию random_numbers(), которая принимает два аргумента:

left — целое число
right — целое число
Функция должна возвращать итератор, генерирующий бесконечную последовательность случайных целых чисел в диапазоне от left до right включительно.

Примечание 1. Гарантируется, что left <= right.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый итератор random_numbers(), но не код, вызывающий его.
'''
from random import randrange


def random_numbers(left, right):
    return iter(lambda: randrange(left, right + 1), left - 1)


# INPUT DATA:

# TEST_1:
iterator = random_numbers(1, 1)

print(next(iterator))
print(next(iterator))

# TEST_2:
iterator = random_numbers(1, 10)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))

# TEST_3:
iterator = random_numbers(-100, -92)

print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))

# TEST_4:
iterator = random_numbers(5, 5)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# TEST_5:
iterator = random_numbers(1000, 1001)

print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))

# TEST_6:
iterator = random_numbers(-100, 99)

print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))