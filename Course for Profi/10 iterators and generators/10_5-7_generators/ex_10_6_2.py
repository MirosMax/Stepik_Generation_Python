'''
Функция is_prime()
Реализуйте функцию is_prime() с использованием генераторных выражений, которая принимает один аргумент:

number — натуральное число
Функция должна возвращать True, если число number является простым, или False в противном случае.

Примечание 1. Простое число — натуральное число, имеющее ровно два различных натуральных делителя — единицу и самого себя.

Примечание 2. В задаче удобно воспользоваться функциями all() или any().

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_prime(), но не код, вызывающий ее.
'''


def is_prime(number):
    if number == 1:
        return False
    return all(number % i for i in range(2, number))


# INPUT DATA:

# TEST_1:
print(is_prime(7))

# TEST_2:
print(is_prime(8))

# TEST_3:
print(is_prime(1))

# TEST_4:
print(is_prime(16))

# TEST_5:
print(is_prime(27))

# TEST_6:
print(is_prime(13))

# TEST_7:
print(is_prime(421))

# TEST_8:
print(is_prime(1061))

# TEST_9:
print(is_prime(9973))