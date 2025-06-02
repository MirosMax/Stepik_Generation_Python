'''
Декоратор do_twice
Реализуйте декоратор do_twice, вызывающий декорируемую функцию два раза.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор do_twice, но не код, вызывающий его.
'''


def do_twice(func):
    def wrapper(*args, **kwargs):
        for _ in range(2):
            res = func(*args, **kwargs)
        return res

    return wrapper


# INPUT DATA:

# TEST_1:
@do_twice
def beegeek():
    print('beegeek')


beegeek()


# TEST_2:
@do_twice
def beegeek():
    print('beegeek')


print(beegeek())


# TEST_3:
@do_twice
def beegeek():
    return 'beegeek'


print(beegeek())


# TEST_4:
@do_twice
def beegeek():
    print('beegeek')


beegeek()
beegeek()
beegeek()


# TEST_5:
@do_twice
def beegeek(a, b, sep):
    print(a + b + sep)


beegeek(1, 2, sep=10)


# TEST_6:
@do_twice
def beegeek(*args, **kwargs):
    print('beegeek' * sum(args + tuple(kwargs.values())))


beegeek(1, 1, 1, sep=1, end=2, step=3)