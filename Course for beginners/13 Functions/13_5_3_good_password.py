# объявление функции
def is_password_good(password):
    if len(password) >= 8:
        for c in password:
            if c.isalpha() and c.isupper():
                break  # если нашли первую букву в верхнем регистре, переходим к след.циклу
        else:
            return False
        for c in password:
            if c.isalpha() and c.islower():
                break  # если нашли первую букву в нижнем регистре, переходим к след.циклу
        else:
            return False
        for c in password:
            if c.isdigit():
                break  # если нашли первую цифру, останавливаем последний цикл (все нужные условия к этому моменту выполнены)
        else:
            return False
    else:
        return False
    return True   # True вернется только если все условия выполнены, в противном случае False при первом несовпадении любого условия, и дальнейшие проверки закончатся


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
