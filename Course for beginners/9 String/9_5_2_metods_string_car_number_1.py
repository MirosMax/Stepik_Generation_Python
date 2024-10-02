#  мой первый вариант решения

num = input()
alpha = 'АВЕКМНОРСТУХ'

if 9 <= len(num) <= 10 and num[6] == '_' and (num[0] in alpha) and num[1:4].isdigit() and (num[4] in alpha) and (num[5] in alpha) and num[7:10].isdigit():
    print('YES')
else:
    print('NO')
