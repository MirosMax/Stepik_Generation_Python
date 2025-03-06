'''
ТЧМ
Во многих музеях существует один день месяца, когда посещение музея для всех лиц или отдельных категорий
граждан происходит без взимания платы. Например, в Эрмитаже это третий четверг месяца.

Напишите программу, которая определяет даты бесплатных дней посещения Эрмитажа в заданном году.

Формат входных данных
На вход программе подается натуральное число, представляющее год.

Формат выходных данных
Программа должна определить все даты бесплатных дней посещения Эрмитажа в введенном году и вывести их. Даты
должны быть расположены в порядке возрастания, каждая на отдельной строке, в формате DD.MM.YYYY.

Примечание. Тестовые данные доступны по ссылкам:
Архив с тестами https://stepik.org/media/attachments/lesson/570049/tests_2361914.zip
GitHub https://github.com/python-generation/Professional/tree/main/Module_3/Module_3.7/Module_3.7.14
'''


def get_all_third_thursday(y):
    import calendar
    from datetime import datetime, timedelta

    result = []
    for m in range(1, 13):
        start = datetime(year=y, month=m, day=1)
        while True:
            if start.weekday() == calendar.THURSDAY:
                break
            start += timedelta(days=1)
        result.append((start + timedelta(days=14)).strftime('%d.%m.%Y'))

    return result


print(*get_all_third_thursday(int(input())), sep='\n')
