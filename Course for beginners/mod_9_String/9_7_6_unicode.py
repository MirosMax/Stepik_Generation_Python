comment = input()
old_pay = 0
new_pay = 0

alpha_en = 'eyopaxcETOPAHXCBM'
alpha_ru = 'еуорахсЕТОРАНХСВМ'

for c in comment:
    old_pay += ord(c)
    if c in alpha_en:
        c = alpha_ru[alpha_en.find(c)]  # Находим индекс заменяемого символа и присваиваем новое значению символу
    new_pay += ord(c)

print(f'''Старая стоимость: {old_pay * 3}🐝
Новая стоимость: {new_pay * 3}🐝''')
