'''
Результаты экзамена 🌶️
Вам доступен файл exam_results.csv, который содержит информацию о прошедшем экзамене в некотором учебном заведении. В первом столбце записано имя студента, во втором — фамилия, в третьем — оценка за экзамен, в четвертом — дата и время сдачи в формате YYYY-MM-DD HH:MM:SS, в пятом — адрес электронной почты:

name,surname,score,date_and_time,email
Jayson,Edwards,2,2021-11-10 10:00:00,sonnen@yahoo.com
April,Sims,3,2021-11-01 11:00:00,retoh@outlook.com
...
Каждый студент имеет право пересдать экзамен два раза, поэтому он может встречаться в исходном файле до трёх раз с различной оценкой и различными датой и временем сдачи.

Напишите программу, которая для каждого студента определяет его максимальную оценку, а также дату и время ее получения. Программа должна создать список словарей, каждый из которых содержит следующие пары ключ-значение:

name — имя студента
surname — фамилия студента
best_score — максимальная оценка за экзамен
date_and_time — дата и время получения максимальной оценки в исходном формате
email — адрес электронной почты
Полученный список программа должна записать в файл best_scores.json, причем словари в списке должны быть расположены в лексикографическом порядке названий электронных почт. Порядок ключей в словарях при этом не важен.

Примечание 1. Если при пересдаче студент получил такую же оценку, что и в прошлый раз, то в качестве даты следует указать дату пересдачи.

Примечание 2. В качестве разделителя в файле exam_results.csv используется запятая, при этом кавычки не используются.

Примечание 3. Начальная часть файла best_scores.json выглядит так:

[
   {
      "name": "Stephen",
      "surname": "Farley",
      "best_score": 3,
      "date_and_time": "2021-11-12 12:00:00",
      "email": "aardo@mac.com"
   },
   {
      "name": "Kaylen",
      "surname": "Horne",
      "best_score": 4,
      "date_and_time": "2021-11-09 11:00:00",
      "email": "aaribaud@att.net"
   },
   ...
]
Примечание 4. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/623073/exam_results.csv
https://stepik.org/media/attachments/lesson/623073/clue_exam_results.txt

Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.
'''

import csv
import json
from datetime import datetime

with open('exam_results.csv', 'r', encoding='utf8') as file:
    data = sorted(
        csv.DictReader(file),
        key=lambda x: datetime.fromisoformat(x['date_and_time'])
    )
    result = {}
    for student in data:
        if student['email'] in result:
            score = int(student['score'])
            if score >= result[student['email']]['best_score']:
                result[student['email']]['best_score'] = score
                result[student['email']]['date_and_time'] = student['date_and_time']
        else:
            result[student['email']] = {
                'name': student['name'],
                'surname': student['surname'],
                'best_score': int(student['score']),
                'date_and_time': student['date_and_time'],
                'email': student['email']
            }

with open('best_scores.json', 'w', encoding='utf8', newline='') as file:
    json.dump(
        sorted(result.values(), key=lambda x: x['email']),
        file,
        indent=3
    )
