'''
Функция is_good_password() 🐍
Назовем пароль хорошим, если
его длина равна 9 или более символам
в нем присутствуют большие и маленькие буквы любого алфавита
в нем имеется хотя бы одна цифра

Реализуйте функцию is_good_password() в стиле EAFP, которая принимает один аргумент:

string — произвольная строка
Функция должна возвращать True, если строка string представляет собой хороший пароль, или возбуждать
исключение:

LengthError, если его длина меньше
9
9 символов
LetterError, если в нем отсутствуют буквы или все буквы имеют одинаковый регистр
DigitError, если в нем нет ни одной цифры
Примечание 1. Исключения LengthError, LetterError и DigitError уже определены и доступны.

Примечание 2. Приоритет возбуждения исключений в случае невыполнения нескольких условий: LengthError,
затем LetterError, а уже после DigitError.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию
is_good_password(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами https://stepik.org/media/attachments/lesson/640052/tests_2712437.zip
GitHub https://github.com/python-generation/Professional/tree/main/Module_7/Module_7.5/Module_7.5.8
Sample Input 1:

try:
    print(is_good_password('Short7'))
except Exception as err:
    print(type(err))
Sample Output 1:

<class '__main__.LengthError'>
Sample Input 2:

print(is_good_password('еПQSНгиfУЙ70qE'))
Sample Output 2:

True
Sample Input 3:

try:
    print(is_good_password('41157081231232'))
except Exception as err:
    print(type(err))
Sample Output 3:

<class '__main__.LetterError'>
'''

class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass


def is_good_password(psw):
    if len(psw) < 9:
        raise LengthError
    elif any([not any(a.isalpha() for a in psw), psw.isupper(), psw.islower()]):
        raise LetterError
    elif not any([a.isdigit() for a in psw]):
        raise DigitError
    else:
        return True


try:
    print(is_good_password('abc!@#%$#%#$%^&dABC8'))
except Exception as err:
    print(type(err))
