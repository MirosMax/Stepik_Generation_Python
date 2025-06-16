'''
Функция pairwise()
Реализуйте генераторную функцию, которая принимает один аргумент:

iterable — итерируемый объект
Функция должна возвращать генератор, порождающий последовательность кортежей, каждый из которых содержит очередной элемент итерируемого объекта iterable, а также следующий за ним элемент:

(<очередной элемент>, <следующий элемент>)
Для последнего элемента следующим считается значение None.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию pairwise(), но не код, вызывающий ее.
'''


def pairwise(iterable):
    iterable = iter(iterable)
    try:
        current_el, next_el = None, next(iterable)
    except StopIteration:
        return iterable
    while True:
        try:
            current_el = next_el
            next_el = next(iterable)
            yield current_el, next_el
        except StopIteration:
            next_el = None
            break
    yield current_el, next_el


# INPUT DATA:

# TEST_1:
numbers = [1, 2, 3, 4, 5]

print(*pairwise(numbers))

# TEST_2:
iterator = iter('stepik')

print(*pairwise(iterator))

# TEST_3:
print(list(pairwise([])))

# TEST_4:
data = map(abs, range(-100, 100))

print(*pairwise(data))

# TEST_5:
data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')

print(*pairwise(data))

# TEST_6:
data = 'JSKFJSDIFjejfkdjKJFIOJfkgkSDJGIEJGsklGDnvmmcvlwoqeriwjndSKF'

print(*pairwise(data))

# TEST_7:
iterator = pairwise('A')

print(next(iterator))

# TEST_8:
data = ['bee', 'geek', 'stepik', 'python']

print(*pairwise(data))