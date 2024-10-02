# объявление функции
def get_month(language, number):
    ru_month = [
        'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
        'ноябрь', 'декабрь'
    ]
    en_month = [
        'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
        'November', 'December'
    ]
    if language == 'ru':
        return ru_month[number - 1]
    elif language == 'en':
        return en_month[number - 1].lower()

# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))
