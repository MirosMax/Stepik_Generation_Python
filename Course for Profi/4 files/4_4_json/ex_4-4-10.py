'''
Я исповедую Python, а ты?
Вам доступен файл countries.json, содержащий список JSON-объектов c информацией о странах и исповедуемых в
них религиях:

[
   {
      "country": "Afghanistan",
      "religion": "Islam"
   },
   {
      "country": "Albania",
      "religion": "Islam"
   },
   ...
]
Каждый объект из этого списка содержит два атрибута:

country — страна
religion — исповедуемая религия
Напишите программу, которая создает единственный JSON-объект, имеющий в качестве ключа название религии, а
в качестве значения — список стран, в которых исповедуется данная религия. Полученный JSON-объект программа
должна записать в файл religion.json.

Примечание 1. Страны в списках должны располагаться в своем исходном порядке.

Примечание 2. Начальная часть файла religion.json выглядит так:

{
   "Islam":[
      "Afghanistan",
      "Albania",
      "Algeria",
      ...
   ],
   ...
}
Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/623073/countries.json
https://stepik.org/media/attachments/lesson/623073/clue_religion.txt

Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
'''

import json

with open('countries.json', 'r', encoding='utf8') as file:
    religion = {}
    data = json.load(file)

    for row in data:
        religion[row['religion']] = religion.get(row['religion'], []) + [row['country']]

with open('religion.json', 'w', encoding='utf8', newline='') as file:
    json.dump(religion, file, indent=3)