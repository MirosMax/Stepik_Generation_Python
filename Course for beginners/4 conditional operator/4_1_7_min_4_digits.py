a, b, c, d = int(input()), int(input()), int(input()), int(input())

m = a  # задаем 4 переменную, которая будет отвечать на мин.значение
if b < m:
    m = b
if c < m:
    m = c
if d < m:
    m = d

print(m)
