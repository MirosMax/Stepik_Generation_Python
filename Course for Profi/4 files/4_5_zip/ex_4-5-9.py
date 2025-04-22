'''
Шахматы были лучше 🌶️
Вам доступен архив data.zip, содержащий различные папки и файлы. Среди них есть несколько JSON файлов,
каждый из которых содержит информацию о каком-либо футболисте:

{
   "first_name": "Gary",
   "last_name": "Cahill",
   "team": "Chelsea",
   "position": "Defender"
}
У футболиста имеются следующие атрибуты:

first_name — имя
last_name — фамилия
team — название футбольного клуба
position — игровая позиция
Напишите программу, которая обрабатывает только данные JSON файлы и выводит имена и фамилии футболистов,
выступающих за футбольный клуб Arsenal. Футболисты должны быть расположены в лексикографическом порядке
имен, а при совпадении — в лексикографическом порядке фамилий, каждый на отдельной строке.

Примечание 1. Обратите внимание, что наличие у файла расширения .json не гарантирует, что он является
корректным текстовым файлом в формате JSON. Для того чтобы определить, является ли файл корректным текстовым
файлом в формате JSON, воспользуйтесь конструкцией try-except и функцией is_correct_json() из предыдущего
урока.

Примечание 2. Начальная часть ответа выглядит так:

Alex Iwobi
Alexis Sanchez
...
Примечание 3. Указанный архив доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/547172/data.zip
https://stepik.org/media/attachments/lesson/547172/clue_json.txt
'''

import json
from zipfile import ZipFile


with ZipFile('data.zip') as zip_file:
    jsons = filter(lambda a: a.filename.endswith('.json'), zip_file.infolist())
    players = []
    for item in jsons:
        with zip_file.open(item.filename, 'r') as file:
            data = file.read().decode(encoding='utf8', errors='ignore')
            if '"team": "Arsenal"' in data:
                data = json.loads(data)
                players.append((data['first_name'], data['last_name']))
    for player in sorted(players, key=lambda a: (a[0], a[1])):
        print(*player)