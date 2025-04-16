'''
Общественное питание 😥
Вам доступен файл food_services.json, содержащий список JSON-объектов, которые представляют данные о заведениях общественного питания:

[
   {
      "Name": "СМЕТАНА",
      "IsNetObject": "нет",
      "OperatingCompany": "",
      "TypeObject": "кафе",
      "AdmArea": "Северо-Восточный административный округ",
      "District": "Ярославский район",
      "Address": "город Москва, улица Егора Абакумова, дом 9",
      "SeatsCount": 48
   },
   ...
]
Под «заведением» будем подразумевать один JSON-объект из этого списка. У заведения имеются следующие атрибуты:

Name — название
IsNetObject — да\нет в зависимости от того, является ли заведение сетевым
OperatingCompany — название сети
TypeObject — вид (кафе, столовая, ресторан и т.д.)
AdmArea — административная зона
District — район
Address — полный адрес
SeatsCount — количество мест
Напишите программу, которая:

определяет район Москвы, в котором находится больше всего заведений, и выводит название этого района и количество заведений в нем
определяет сеть с самым большим числом заведений и выводит название этой сети и количество заведений этой сети
Полученные значения программа должна вывести в следующем формате:

<район>: <количество заведений>
<название сети>: <количество заведений>
Примечание 1. Гарантируется, что искомая сеть единственная.

Примечание 2. Пример вывода:

район Метрогородок: 456
Французская пекарня SeDelice: 144
Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/623073/food_services.json
https://stepik.org/media/attachments/lesson/623073/clue_food1.txt

Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
'''

import json

with open('food_services.json', 'r', encoding='utf8') as file:
    data = json.load(file)
    result = {'Districts': {}, 'Food_names': {}}
    for fs in data:
        result['Districts'][fs['District']] = result.get('Districts').get(fs['District'], 0) + 1
        if fs['IsNetObject'] == 'да':
            result['Food_names'][fs['OperatingCompany']] = result.get('Food_names').get(fs['OperatingCompany'], 0) + 1
    found_distr = max(result['Districts'].items(), key=lambda x: x[1])
    found_fs = max(result['Food_names'].items(), key=lambda x: x[1])
    print(f'{found_distr[0]}: {found_distr[1]}')
    print(f'{found_fs[0]}: {found_fs[1]}')