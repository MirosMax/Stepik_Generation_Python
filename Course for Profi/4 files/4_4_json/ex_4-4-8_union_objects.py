'''
Объединение объектов
Вам доступны два файла data1.json и data2.json, каждый из которых содержит по единственному JSON-объекту:

{
   "Holly-Anne": [
      33,
      "failed"
   ],
   "Caty": [
      36,
      "failed"
   ],
   ...
}
Напишите программу, которая объединяет два данных JSON-объекта в один JSON-объект, причем если пары из первого и второго объектов имеют совпадающие ключи, то значение следует взять из второго объекта. Полученный JSON-объект программа должна записать в файл data_merge.json.

Примечание 1. Например, если бы файлы data1.json и data2.json имели вид:

{
   "Timur": 99,
   "Anri": 97
}
{
   "Dima": 99,
   "Anri": 100
}
то программа должна была бы создать файл data_merge.json со следующим содержанием:

{
   "Anri": 100,
   "Dima": 99,
   "Timur": 99
}
Примечание 2. Элементы в результирующем JSON-объекте могут располагаться в произвольном порядке.

Примечание 3. Указанные файлы доступны по ссылке и ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/623073/data1.json
https://stepik.org/media/attachments/lesson/623073/data2.json
https://stepik.org/media/attachments/lesson/623073/clue_data_merge.txt

Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
'''

import json

with (
    open('data3.json', 'r', encoding='utf8') as file1,
    open('data4.json', 'r', encoding='utf8') as file2,
    open('data_merge.json', 'w', encoding='utf8', newline='') as write_file
):
    data = json.load(file1) | json.load(file2)  # слияние двух словарей с заменой одинаковых ключ: значение
    json.dump(data, write_file, indent='   ')

