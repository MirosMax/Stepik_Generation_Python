'''
Вам доступны три списка names, budgets и box_offices. Первый список содержит названия различных мультфильмов,
второй и третий — соответствующие бюджеты и сборы в долларах.

Дополните приведенный ниже код, чтобы он определил, какую прибыль принес каждый мультфильм, и вывел названия
мультфильмов, указав для каждого соответствующую прибыль. Мультфильмы должны быть расположены в лексикографическом
порядке, каждый на отдельной строке, в следующем формате:

<фильм>: <прибыль>$
Примечание 1. Прибыль определяется как разность сборов и бюджета.

Примечание 2. Начальная часть ответа выглядит так:

Cars: 342216280$
Coco: 627082196$
Finding Nemo: 846335536$
...
Примечание 3. В задаче удобно воспользоваться функцией zip().
'''

names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
budgets = [150000000, 120000000, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
box_offices = [643331111, 462216280, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]

for i in sorted(zip(names, budgets, box_offices)):
    print(f'{i[0]}: {i[2] - i[1]}$')


