'''
Функция verification()
Реализуйте функцию verification(), которая проверяет правильность введенного пароля. Она должна принимать четыре
аргумента в следующем порядке:

login — логин пользователя
password — пароль пользователя
success — некоторая функция
failure — некоторая функция
Пароль считается правильным, если в нем присутствует, хотя бы одна заглавная латинская буква, хотя бы одна строчная
латинская буква и хотя бы одна цифра. Функция verification() должна вызывать функцию success() с аргументом login,
если переданный пароль является правильным, иначе — функцию failure() с аргументами login и строкой-сообщением об
ошибке:

в пароле нет ни одной буквы, если в пароле отсутствуют латинские буквы
в пароле нет ни одной заглавной буквы, если в пароле отсутствуют заглавные латинские буквы
в пароле нет ни одной строчной буквы, если в пароле отсутствуют строчные латинские буквы
в пароле нет ни одной цифры, если в пароле отсутствуют цифры
Примечание 1. Если пароль не удовлетворяет нескольким условиям, то приоритеты выбора строки-сообщения об ошибке
являются следующими:

в пароле нет ни одной буквы
в пароле нет ни одной заглавной буквы
в пароле нет ни одной строчной буквы
в пароле нет ни одной цифры
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию verification(), но не
код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами https://stepik.org/media/attachments/lesson/640036/tests_2670414.zip
GitHub https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.3/Module_9.3.18
Sample Input 1:

def success(login):
    print(f'Привет, {login}!')

def failure(login, text):
    print(f'{login}, попробуйте снова. Ошибка: {text}')

verification('timyrik20', 'Beegeek314', success, failure)
Sample Output 1:

Привет, timyrik20!
Sample Input 2:

def success(login):
    print(f'Здравствуйте, {login}!')

def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')

verification('Ruslan_Chaniev', 'stepikstepik2', success, failure)
Sample Output 2:

Ruslan_Chaniev, попробуйте снова. Текст ошибки: в пароле нет ни одной заглавной буквы
'''


def verification(login, password, success, failure):
    flags = {
        'no_alpha': [True, 'в пароле нет ни одной буквы'],
        'no_upper': [True, 'в пароле нет ни одной заглавной буквы'],
        'no_lower': [True, 'в пароле нет ни одной строчной буквы'],
        'no_digit': [True, 'в пароле нет ни одной цифры'],
    }

    for char in password:
        if char.isdigit():
            flags['no_digit'][0] = False
        if char.isalpha() and char.isascii():
            flags['no_alpha'][0] = False
            if char.isupper():
                flags['no_upper'][0] = False
            else:
                flags['no_lower'][0] = False

    for i in flags.values():
        if i[0]:
            failure(login, i[1])
            break
    else:
        success(login)


def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'мойпароль123', success, failure)