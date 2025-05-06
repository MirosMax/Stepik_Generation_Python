'''
Бесплатные курсы берут свое 😢
Для дополнительного заработка Тимур решил заняться продажей овощей. У него имеются данные о продажах за
год, разделенные на четыре файла по кварталам: quarter1.csv, quarter2.csv, quarter3.csv и quarter4.csv. В
каждом файле в первом столбце указывается название продукта, а в последующих — количество проданного продукта
в килограммах за определенный месяц:

продукт,январь,февраль,март
Картофель,39,61,3
Дайкон,51,96,83
...
Также присутствует файл prices.json, содержащий словарь, в котором ключом является название продукта, а
значением — цена за килограмм в рублях:

{
   "Картофель": 53,
   "Дайкон": 55,
...
}
Напишите программу, которая выводит единственное число — сумму, заработанную Тимуром за год на продаже овощей.

Примечание 1. Ссылки на указанные файлы: quarter1.csv, quarter2.csv, quarter3.csv, quarter4.csv, prices.json.
Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/635441/quarter1.csv
https://stepik.org/media/attachments/lesson/635441/quarter2.csv
https://stepik.org/media/attachments/lesson/635441/quarter3.csv
https://stepik.org/media/attachments/lesson/635441/quarter4.csv
https://stepik.org/media/attachments/lesson/635441/prices.json
https://stepik.org/media/attachments/lesson/635441/clue_free.txt

Примечание 2. При открытии файла используйте явное указание кодировки UTF-8.
'''
import csv
import json
from collections import Counter

all_products = Counter()
for i in range(1, 5):
    with open(f'quarter{i}.csv', 'r', encoding='utf8') as file_in:
        data = list(csv.reader(file_in))[1:]
        data = Counter({item[0]: sum(int(a) for a in item[1:]) for item in data})
    all_products += data

with open('prices.json', 'r', encoding='utf8') as file_in:
    price_list = json.load(file_in)
    for product, price in price_list.items():
        all_products[product] *= price

print(all_products.total())