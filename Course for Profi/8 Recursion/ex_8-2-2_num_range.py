'''
Напишите программу с использованием рекурсии, которая выводит последовательность натуральных чисел
от 1 до 100 включительно.
'''


def num_range(n):
    if n > 0:
        num_range(n - 1)
        print(n)


num_range(100)
