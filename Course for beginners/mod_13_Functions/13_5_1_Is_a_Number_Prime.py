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


# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))