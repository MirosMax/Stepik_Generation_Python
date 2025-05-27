'''
Функция sort_priority() 🌶️
Реализуйте функцию sort_priority(), которая принимает два аргумента в следующем порядке:

values — список чисел
group — список, кортеж или множество чисел
Функция должна сортировать по неубыванию список чисел values, делая при этом приоритетной группу чисел из group, которая должна следовать первой.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию sort_priority(), но не код, вызывающий ее.
'''


# def sort_priority(values, group):
#     values.sort()
#     for i in sorted(group, reverse=True):
#         if i in values:
#             x = values.pop(values.index(i))
#             values.insert(0, x)


# 2 вариант (преподавательский)
def sort_priority(values, group):
    values.sort(key=lambda x: (x not in group, x))


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
sort_priority(numbers, group)

print(numbers)