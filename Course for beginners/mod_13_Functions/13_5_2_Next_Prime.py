# объявление функции
def get_next_prime(num):
    num += 1
    is_prime = False
    while not is_prime:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                num += 1
                break
        else:
            is_prime = True
    return num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
