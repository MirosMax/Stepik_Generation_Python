'''
Вам доступен словарь data. Дополните приведенный ниже код, чтобы он вывел данный словарь, расположив его
элементы в обратном порядке.

Примечание. Например, если бы словарь data имел вид:

data = OrderedDict(key1='value1', key2='value2', key3='value3')
то программа должна была бы вывести (до Python 3.12):

OrderedDict([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])
в Python 3.12:

OrderedDict({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'})
'''

from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
reverse_data = OrderedDict()
for key, value in reversed(data.items()):
    reverse_data[key] = value

print(reverse_data)



