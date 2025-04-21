'''
Избранные
Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит
названия файлов из этого архива, которые были созданы или изменены позднее 2021-11-30 14:22:00. Названия
файлов должны быть расположены в лексикографическом порядке, каждое на отдельной строке.

Примечание 1. Если файл находится в папке, вывести следует только название без пути.

Примечание 2. Начальная часть ответа выглядит так:

countries.json
data_sample.csv
...
Примечание 3. Указанный архив доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/547172/workbook.zip
https://stepik.org/media/attachments/lesson/547172/clue_dragonborn.txt
'''

from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip') as zip_file:
    # dt = datetime.fromisoformat('2021-11-30 14:22:00')
    dt = datetime.strptime('2021-11-30 14:22:00', '%Y-%m-%d %H:%M:%S')
    result = []
    for f in zip_file.infolist():
        dt_file = datetime(*f.date_time)
        if dt_file > dt and not f.is_dir():
            result.append(f.filename.split('/')[-1])
    print(*sorted(result), sep='\n')
