'''
Дневник космонавта 🌶️
Вам доступен текстовый файл diary.txt, в который космонавт записывал небольшие отчёты за день. Каждый новый отчёт он
мог записать либо в начало файла, либо в середину, либо в конец. Все отчеты разделены между собой пустой строкой.
Каждый новый отчёт начинается со строки с датой и временем в формате DD.MM.YYYY; HH:MM, после которой следуют события,
произошедшие за указанный день:

29.04.2006; 06:55
It wasn’t until several hours after launch that we were able to take the time to get out of our seats and enter the
“habitation module.”
Then, after another orbital maneuver, we finally were able to take a several hour break and get a little sleep.

03.05.2006; 20:24
Everybody had a sleeping bag although I only used mine on a couple of brief occasions, and then only when getting a
little chilly.

...
Напишите программу, которая расставляет все записи космонавта в хронологическом порядке и выводит полученный результат.
'''
from datetime import datetime


with open('diary.txt', 'r', encoding='UTF-8') as file:
    text = file.read()

text = text.split('\n\n')
result = {}
f = '%d.%m.%Y; %H:%M'
for p in text:
    dt = datetime.strptime(p[:p.find('\n')], f)
    result[dt] = p[p.find('\n') + 1:]

for dt in sorted(result):
    print(dt.strftime(f), result[dt], sep='\n')
    print()
