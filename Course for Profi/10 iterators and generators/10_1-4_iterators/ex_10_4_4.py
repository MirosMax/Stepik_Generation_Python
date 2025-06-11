'''
Итератор Fibonacci
Реализуйте класс Fibonacci, порождающий итераторы, конструктор которого не принимает никаких аргументов.

Итератор класса Fibonacci должен генерировать бесконечную последовательность чисел Фибоначчи, начиная с 1.

Примечание 1. Последовательность Фибоначчи – последовательность натуральных чисел, где каждое последующее число является суммой двух предыдущих:

1,1,2,3,5,8,13,21,34

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый класс Fibonacci.
'''


class Fibonacci():
    def __init__(self):
        self.seq = [0, 0, 1]

    def __iter__(self):
        return self

    def __next__(self):
        self.next = sum(self.seq[1:])
        self.seq = self.seq[1:] + [self.next]
        return self.seq[1]


# INPUT DATA:

# TEST_1:
fibonacci = Fibonacci()

print(next(fibonacci))

# TEST_2:
fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))

# TEST_3:
fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))

# TEST_4:
fibonacci = Fibonacci()

for _ in range(50):
    print(next(fibonacci))

# TEST_5:
fibonacci = Fibonacci()

for _ in range(100):
    next(fibonacci)

print(next(fibonacci))

# TEST_6:
fibonacci = Fibonacci()

for _ in range(76):
    next(fibonacci)

next(fibonacci)
next(fibonacci)
next(fibonacci)
next(fibonacci)

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))