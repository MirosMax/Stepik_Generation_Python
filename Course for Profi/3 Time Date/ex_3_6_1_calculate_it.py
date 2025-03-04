import time


def calculate_it(func, *args):
    start = time.time()
    result = func(*args)
    time_spent = time.time() - start
    return result, time_spent


def add(a, b, c):
    time.sleep(3)
    return a + b + c


print(calculate_it(add, 1, 2, 3))