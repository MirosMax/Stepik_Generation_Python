'''
Спортивные площадки
Вам доступен файл playgrounds.csv с информацией о спортивных площадках Москвы. В первом столбце записан
тип площадки,  во втором — административный округ, в третьем — название района, в четвертом — адрес:

ObjectName;AdmArea;District;Address
Парк, озелененная городская территория «Лианозовский парк культуры и отдыха»;Северо-Восточный
административный округ;район Лианозово;Угличская улица, дом 13
...
Напишите программу, создающую JSON-объект, ключом в котором является административный округ, а значением
— JSON-объект, в котором, в свою очередь, ключом является название района, относящийся к этому
административному округу, а значением — список адресов всех площадок в этом районе. Полученный JSON-объект
программа должна записать в файл addresses.json.

Примечание 1. Адреса в списках должны располагаться в своем исходном порядке.

Примечание 2. Разделителем в файле playgrounds.csv является точка с запятой, при этом кавычки не используются.

Примечание 3. Начальная часть файла addresses.json выглядит так:

{
   "Северо-Восточный административный округ": {
      "район Лианозово": [
         "Угличская улица, дом 13",
         "Алтуфьевское шоссе, дом 147А"
      ],
      "район Отрадное": [
         "Алтуфьевское шоссе, дом 20А",
         "Юрловский проезд, дом 8, строение 1",
         "Юрловский проезд, дом 8, строение 1"
      ],
      ...
   },
   ...
}
Примечание 4. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/623073/playgrounds.csv
https://stepik.org/media/attachments/lesson/623073/clue_playgrounds.txt

Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.
'''

import json
import csv

with open('playgrounds.csv', 'r', encoding='utf8') as file:
    playgrounds = csv.DictReader(file, delimiter=';')
    addresses = {}
    for pg in playgrounds:
        addresses.setdefault(pg['AdmArea'], {}).setdefault(pg['District'], []).append(pg['Address'])
        # addresses[pg['AdmArea']] = addresses.get(pg['AdmArea'], {})
        # addresses[pg['AdmArea']][pg['District']] = addresses.get(pg['AdmArea'], {}).get(pg['District'], []) + [pg['Address']]

with open('addresses.json', 'w', encoding='utf8', newline='') as file:
    json.dump(addresses, file, indent=3, ensure_ascii=False)