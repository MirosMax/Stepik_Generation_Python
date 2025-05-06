'''
Зоопарк
Вам доступен файл zoo.json, содержащий список JSON-объектов с данными об обитателях некоторого зоопарка.
Ключом в каждом объекте является название животного, значением — их количество в зоопарке:

[
   {
      "Axolotl": 11,
      "Poison Frog": 12,
      "Sonoran Toad": 6,
      "Tiger Salamander": 16
   },
   {
      "African Fish Eagle": 6,
      "Andean Condor": 8,
      "Black Vulture": 8,
      "Bufflehead Duck": 9,
      "Flamingo": 8,
      "Great Horned Owl": 16,
      "Hornbill": 1
   },
   ...
]
Напишите программу, которая определяет, сколько всего животных обитает в зоопарке, и выводит полученный
результат.

Примечание 1. Гарантируется, что все ключи в JSON-объектах, различны.

Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/634670/zoo.json
https://stepik.org/media/attachments/lesson/634670/clue_zoo.txt

Примечание 3. При открытии файла используйте явное указание кодировки UTF-8.
'''

import json

# # Вариант решения 1
# from collections import Counter
#
# with open('zoo.json', 'r', encoding='utf8') as file_in:
#     data = json.load(file_in)
#     total = 0
#     for zoo in data:
#         total += Counter(zoo).total()
# print(total)

# Вариант решения 2
from collections import ChainMap

with open('zoo.json', 'r', encoding='utf8') as file_in:
    print(sum(ChainMap(*json.load(file_in)).values()))