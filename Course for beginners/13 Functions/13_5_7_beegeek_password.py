'''
BEEGEEK наконец-то открыл свой банк, в котором используются специальные банкоматы с необычным паролем.

Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK
фанатеет от математики, то он решил:

число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть четным.

Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password
и возвращает значение True, если пароль является действительным паролем BEEGEEK банка, или False в противном случае.
'''


# объявление функции
def is_prime(num):
    flag = True
    if num == 1:
        flag = False
        return flag
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            flag = False
            break
    return flag


def is_valid_password(psw):
    if psw.count(':') == 2:
        part_a = psw[:psw.find(':')]
        part_b = int(psw[(psw.find(':') + 1):psw.rfind(':')])
        part_c = int(psw[(psw.rfind(':') + 1):])
        count = 0
        if part_a == part_a[::-1]:
            count += 1
        else:
            return False
        if is_prime(part_b):
            count += 1
        else:
            return False
        if part_c % 2 == 0:
            count += 1
        if count == 3:
            return True
        else:
            return False
    else:
        return False

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
