'''
Итератор Square
Реализуйте класс Square, порождающий итераторы, конструктор которого принимает один аргумент:

n — натуральное число,
Итератор класса Square должен генерировать последовательность из n чисел, каждое из которых является квадратом очередного натурального числа, а затем возбуждать исключение StopIteration.

Примечание 1. Последовательность квадратов натуральных чисел начинается с квадрата числа 1.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый класс Square.
'''
class Square():
    def __init__(self, n):
        self.n = n
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.n:
            raise StopIteration
        else:
            self.index += 1
            return self.index ** 2


# INPUT DATA:

# TEST_1:
squares = Square(2)

print(next(squares))
print(next(squares))

# TEST_2:
squares = Square(10)

print(list(squares))

# TEST_3:
squares = Square(1)

print(list(squares))

# TEST_4:
squares = Square(5)

next(squares)
next(squares)
next(squares)
next(squares)
next(squares)

try:
    next(squares)
except StopIteration:
    print('Error')

# TEST_5:
squares = Square(9)

print(*squares)

# TEST_6:
squares = Square(2)

try:
    print(next(squares))
    print(next(squares))
    print(next(squares))
except:
    print('Error')