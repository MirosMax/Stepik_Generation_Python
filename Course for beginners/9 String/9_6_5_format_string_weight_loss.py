day, weight = int(input()), float(input())

lose_weight_per_day = (100 - 88) / 60

if weight <= (100 - lose_weight_per_day * day):
    print('Все идет по плану')
    print(f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {100 - lose_weight_per_day * day} кг')
else:
    print('Что-то пошло не так')
    print(f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {100 - lose_weight_per_day * day} кг')
