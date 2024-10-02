'''
Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре»
https://ru.wikipedia.org/wiki/CamelCase и преобразует его в «змеиный регистр» https://ru.wikipedia.org/wiki/Snake_case.
'''

# объявление функции
def convert_to_python_case(text):
    snake_case = text[0].lower()
    for c in text[1:]:
        if c.islower() or c.isdigit():
            snake_case += c
        elif c.isupper():
            snake_case += '_' + c.lower()
    return snake_case

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))