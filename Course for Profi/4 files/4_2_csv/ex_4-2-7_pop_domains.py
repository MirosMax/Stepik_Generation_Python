'''
Популярные домены
Вам доступен файл data.csv, который содержит неповторяющиеся данные о пользователях некоторого ресурса. В
первом столбце записано имя пользователя, во втором — фамилия, в третьем — адрес электронной почты:

first_name,surname,email
John,Wilson,johnwilson@outlook.com
Mary,Wilson,marywilson@list.ru
...
Напишите программу, которая создает файл domain_usage.csv, имеющий следующее содержание:

domain,count
rambler.ru,24
iCloud.com,29
...
где в первом столбце записано название почтового домена, а во втором — количество пользователей, использующих
данный домен. Домены в файле должны быть расположены в порядке возрастания количества их использований, при
совпадении количества использований — в лексикографическом порядке.

Примечание 1. Разделителем в файле data.csv является запятая, при этом кавычки не используются.

Примечание 2. Указанный файл доступен по ссылке https://stepik.org/media/attachments/lesson/518491/data.csv
Ответ на задачу доступен по ссылке https://stepik.org/media/attachments/lesson/518491/clue_domains.txt

Примечание 3. Начальная часть файла domain_usage.csv выглядит так:

domain,count
rambler.ru,24
iCloud.com,29
...
Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
'''

import csv


with open('data.csv', 'r', encoding='utf-8') as csv_file:
    data = csv.DictReader(csv_file)
    result = {}
    for row in data:
        domain = row['email'].split('@')[1]
        result[domain] = result.get(domain, 0) + 1

sort_result = sorted(result.items(), key=lambda x: (x[1], x[0]))

with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as csv_file:
    data = csv.writer(csv_file)
    data.writerow(['domain', 'count'])
    data.writerows(sort_result)