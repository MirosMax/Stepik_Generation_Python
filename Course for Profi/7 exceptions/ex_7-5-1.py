'''
Функция is_good_password() 👀
Назовем пароль хорошим, если

его длина равна 9 или более символам
в нем присутствуют большие и маленькие буквы любого алфавита
в нем имеется хотя бы одна цифра
Реализуйте функцию is_good_password() в стиле LBYL, которая принимает один аргумент:

string — произвольная строка
Функция должна возвращать True, если строка string представляет собой хороший пароль, или False в противном
случае.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию
is_good_password(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами https://stepik.org/media/attachments/lesson/640052/tests_2712434.zip
GitHub https://github.com/python-generation/Professional/tree/main/Module_7/Module_7.5/Module_7.5.7
Sample Input 1:

print(is_good_password('41157082'))
Sample Output 1:

False
Sample Input 2:

print(is_good_password('мойпарольсамыйлучший'))
Sample Output 2:

False
Sample Input 3:

print(is_good_password('МойПарольСамыйЛучший111'))
Sample Output 3:

True
'''

# # 1 вариант
# def is_good_password(psw):
#     if (
#         len(psw) >= 9 and
#         any([a.isdigit() for a in psw]) and
#         any([a.isupper() for a in psw]) and
#         any([a.islower() for a in psw])
#     ):
#         return True
#     else:
#         return False


# 2 вариант
def is_good_password(psw):
    if all(
            [len(psw) >= 9,
                any(a.isdigit() for a in psw),
                any(a.isupper() for a in psw),
                any(a.islower() for a in psw)
             ]
    ):
        return True
    else:
        return False


print(is_good_password('41157082'))
print(is_good_password('мойпарольсамыйлучший'))
print(is_good_password('МойПарольСамыйЛучший111'))