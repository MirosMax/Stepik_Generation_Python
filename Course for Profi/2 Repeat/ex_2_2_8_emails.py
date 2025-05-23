'''
Корпоративная почта 🌶️
В онлайн-школе "BEEGEEK" сотрудникам положена корпоративная почта, которая формируется как <имя-фамилия>@beegeek.bzz,
например, timyr-guev@beegeek.bzz. При таком подходе существует проблема тёзок. Для решения такой проблемы было решено
приписывать справа номер.

Тогда первый Тимур Гуев получает ящик timyr-guev@beegeek.bzz (без номера), второй — timyr-guev1@beegeek.bzz,
третий — timyr-guev2@beegeek.bzz, и так далее.

Вам дан список уже занятых ящиков в порядке их выдачи и имена-фамилии новых сотрудников в заранее подготовленном виде
(латиницей с символом - между ними). Напишите программу, которая раздает корпоративные ящики новым сотрудникам школы.

Формат входных данных
На вход программе в первой строке подается целое неотрицательное число n — количество выданных ящиков. В следующих
n строках перечислены сами ящики в порядке выдачи, по одному на строке. На следующей строке задано целое
неотрицательное число m — количество новых сотрудников, которым нужно раздать корпоративные ящики. Каждая из
последующих m строк представляет собой имя и фамилию сотрудника в подготовленном к использованию формате.

Формат выходных данных
Программа должна вывести почтовые ящики (m строк) для новых сотрудников в том порядке, в котором они раздавались.

Примечание. Тестовые данные доступны по ссылкам:
https://github.com/python-generation/Professional/tree/main/Module_2/Module_2.2/Module_2.2.8

Sample Input 1:
6
ivan-petrov@beegeek.bzz
petr-ivanov@beegeek.bzz
ivan-petrov1@beegeek.bzz
ivan-ivanov@beegeek.bzz
ivan-ivanov1@beegeek.bzz
ivan-ivanov2@beegeek.bzz
3
ivan-ivanov
petr-petrov
petr-ivanov

Sample Output 1:
ivan-ivanov3@beegeek.bzz
petr-petrov@beegeek.bzz
petr-ivanov1@beegeek.bzz

Sample Input 2:
2
timyr-guev2@beegeek.bzz
anri-tabuev@beegeek.bzz
3
timyr-guev
timyr-guev
anri-tabuev

Sample Output 2:
timyr-guev@beegeek.bzz
timyr-guev1@beegeek.bzz
anri-tabuev1@beegeek.bzz
'''

logins = {}
for _ in range(int(input())):
    login = input().split('@')[0]
    if login[-1].isdigit():
        num = login[-1]
        login = login[:len(login) - 1]
        logins[login] = logins.get(login, []) + [num]
    else:
        logins[login] = logins.get(login, []) + ['0']

for _ in range(int(input())):
    new_login = input()
    if new_login in logins.keys():
        index = 0
        while True:
            if str(index) in logins[new_login]:
                index += 1
            else:
                break

        logins[new_login] = logins.get(new_login) + [str(index)]
    else:
        logins[new_login] = ['0']
        index = 0

    if index == 0:
        print(new_login + '@beegeek.bzz')
    else:
        print(new_login + str(index) + '@beegeek.bzz')

