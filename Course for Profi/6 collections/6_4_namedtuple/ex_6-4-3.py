'''
Вам доступен именованный кортеж Animal, который содержит данные о животном. Первым элементом именованного
кортежа является имя животного, вторым — семейство, третьим — пол, четвертым — цвет. Также доступен файл
data.pkl, содержащий сериализованный список таких кортежей.

Дополните приведенный ниже код, чтобы для каждого кортежа из этого списка он вывел названия его полей и
значения этих полей в следующем формате:

name: <значение>
family: <значение>
sex: <значение>
color: <значение>
Между полями и значениями двух разных кортежей должна располагаться пустая строка.

Примечание 1. Сначала должно следовать содержание первого кортежа из списка, затем второго, и так далее.

Примечание 2. Например, если бы файл data.pkl содержал следующий сериализованный список:

[Animal(name='Alex', family='dogs', sex='m', color='brown'),
Animal(name='Nancy', family='dogs', sex='w', color='black')]
то программа должна была бы вывести:

name: Alex
family: dogs
sex: m
color: brown

name: Nancy
family: dogs
sex: w
color: black
 Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
 https://stepik.org/media/attachments/lesson/740203/data.pkl
 https://stepik.org/media/attachments/lesson/740203/clue_animals.txt
'''

import pickle
from collections import namedtuple

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('data.pkl', 'rb') as file_in:
    data = pickle.load(file_in)
    print(
        *map(lambda x: f'''name: {x.name}\nfamily: {x.family}\nsex: {x.sex}\ncolor: {x.color}''', data),
        sep='\n\n'
    )
