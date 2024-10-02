#  повтор решения препода

num = input()
correct_alpha = 'АВЕКМНОРСТУХ'
flag = 'NO'

if 9 <= len(num) <= 10 and num[6] == '_':
    alpha = num[0] + num[4:6]
    digit = num[1:4] + num[7:]
    if digit.isdigit():
        flag = 'YES'

    for c in alpha:
        if c not in correct_alpha:
            flag = 'NO'
            break
print(flag)