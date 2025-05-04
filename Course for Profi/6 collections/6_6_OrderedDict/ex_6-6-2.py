'''
Вам доступен словарь data с четным количеством элементов. Дополните приведенный ниже код, чтобы он вывел
данный словарь, расположив его элементы по следующему правилу: первый, последний, второй, предпоследний,
третий, и так далее.

Примечание. Например, если бы словарь data имел вид:

data = OrderedDict(key1='value1', key2='value2', key3='value3', key4='value4')
то программа должна была бы вывести (до Python 3.12):

OrderedDict([('key1', 'value1'), ('key4', 'value4'), ('key2', 'value2'), ('key3', 'value3')])
в Python 3.12:

OrderedDict({('key1', 'value1'), ('key4', 'value4'), ('key2', 'value2'), ('key3', 'value3')})
'''

from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
new_data = OrderedDict()
flag = False

for _ in range(len(data)):
    item = data.popitem(last=flag)
    new_data[item[0]] = item[1]
    flag = not flag

print(new_data)