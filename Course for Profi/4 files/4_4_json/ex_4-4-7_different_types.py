'''
Разные типы
Вам доступен файл data.json, содержащий список различных объектов:

[
   "nwkWXma",
   null,
   {
      "ISgHT": "dIUbf"
   },
   "Pzt",
   "BXcbGVTE",
   ...
]
Напишите программу, которая создает список, элементами которого являются объекты из списка, содержащегося
в файле data.json, измененные по следующим правилам:

если объект является строкой, в его конец добавляется восклицательный знак
если объект является числом, он увеличивается на единицу
если объект является логическим значением, он инвертируется
если объект является списком, он удваивается
если объект является JSON-объектом (словарем), в него добавляется новая пара "newkey": null
если объект является пустым значением (null), он не добавляется
Полученный список программа должна записать в файл updated_data.json.

Примечание 1. Например, если бы файл data.json имел вид:

["Hello", 179, true, null, [1, 2, 3], {"key": "value"}]
то программа должна была бы создать файл updated_data.json со следующим содержанием:

["Hello!", 180, false, [1, 2, 3, 1, 2, 3], {"key": "value", "newkey": null}]
Примечание 2. Указанный файл доступен по ссылке. https://stepik.org/media/attachments/lesson/623073/data.json
Ответ на задачу доступен по ссылке. https://stepik.org/media/attachments/lesson/623073/clue_different_types.txt

Примечание 3. При открытии файла используйте явное указание кодировки UTF-8.
'''

import json

with (
    open('data2.json', 'r', encoding='utf8') as read_file,
    open('updated_data.json', 'w', encoding='utf8', newline='') as write_file
):
    data = json.load(read_file)
    new_data = []
    for elem in data:
        if isinstance(elem, str):
            elem += '!'
        elif isinstance(elem, bool):
            elem = not elem
        elif isinstance(elem, int):
            elem += 1
        elif isinstance(elem, list):
            elem *= 2
        elif isinstance(elem, dict):
            elem['newkey'] = None
        elif elem is None:
            continue
        new_data.append(elem)
    json.dump(new_data, write_file, indent='   ')