# объявление функции
def is_palindrome(text):
    text_without = ''
    for c in text:
        if c.isalpha():
            text_without += c.lower()
        else:
            continue
    if text_without == text_without[::-1]:
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))