'''
Возрастание классов 🌶️
Вам доступен файл student_counts.csv, который содержит данные о количестве учеников в некотором учебном заведении за период
2000
2000 —
2021
2021 г. В первом столбце записан год, в последующих столбцах записан класс и количество учеников в данном классе в этом году:

year,5-Б,3-Б,8-А,2-Г,7-Б,1-Б,3-Г,3-А,2-В,6-Б,6-А,8-Б,8-Г,11-А,2-А,7-А,5-А,2-Б,10-А,11-Б,8-В,4-А,7-В,3-В,1-А,9-А,11-В
2000,19,15,18,29,19,17,26,29,28,30,26,27,27,22,29,19,27,20,16,18,15,27,19,29,22,20,23
2001,21,30,22,19,26,20,24,27,20,30,24,30,29,21,20,19,29,27,23,25,30,30,23,22,22,18,22
...
Напишите программу, которая записывает данную таблицу в файл sorted_student_counts.csv, располагая все столбцы в порядке возрастания классов, при совпадении классов — в порядке возрастания букв.

Примечание 1. Каждый класс содержит номер и букву и записывается в следующем формате:

<номер класса>-<буква класса>
Примечание 2. Разделителем в файле student_counts.csv является запятая, при этом кавычки не используются.

Примечание 3. Указанный файл доступен по ссылке. https://stepik.org/media/attachments/lesson/518491/student_counts.csv
Ответ на задачу доступен по ссылке. https://stepik.org/media/attachments/lesson/518491/clue_grades.txt

Примечание 4. Начальная часть файла sorted_student_counts.csv выглядит так:

year,1-А,1-Б,2-А,2-Б,...
2000,22,17,29,20,...
2001,22,20,20,27,...
...
Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.
'''

import csv


with open('student_counts.csv', 'r', encoding='utf-8') as read_file, open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as write_file:
    data = csv.DictReader(read_file)
    new_fieldnames = sorted(data.fieldnames[1:], key=lambda a: (int(a.split('-')[0]), a.split('-')[1]))
    new_fieldnames.insert(0, 'year')

    writer = csv.DictWriter(write_file, fieldnames=new_fieldnames)
    writer.writeheader()
    writer.writerows(data)