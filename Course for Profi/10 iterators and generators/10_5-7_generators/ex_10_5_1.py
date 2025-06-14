'''
Функция simple_sequence()
Реализуйте генераторную функцию simple_sequence(), которая не принимает никаких аргументов.

Функция должна возвращать генератор, порождающий бесконечную возрастающую последовательность натуральных чисел, в которой каждое число встречается столько раз, каково оно:
1,2,2,3,3,3,4,4,4,4,..
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую генераторную функцию simple_sequence(), но не код, вызывающий ее.
'''
def simple_sequence():
    num = 1
    while True:
        for _ in range(num):
            yield num
        num += 1


# INPUT DATA:

# TEST_1:
generator = simple_sequence()

print(next(generator))
print(next(generator))

# TEST_2:
generator = simple_sequence()
numbers = [next(generator) for _ in range(10)]

print(*numbers)

# TEST_3:
generator = simple_sequence()

for _ in range(100):
    print(next(generator))

# TEST_4:
generator = simple_sequence()

for _ in range(1000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# TEST_5:
generator = simple_sequence()

for _ in range(10_000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# TEST_6:
generator = simple_sequence()

for _ in range(10_000_000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))