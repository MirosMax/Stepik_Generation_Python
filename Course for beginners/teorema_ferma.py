e = 0
f = 0
for a in range(1, 151):
    for b in range(a + 1, 151):
        for c in range(b + 1, 151):
            for d in range(c + 1, 151):
                e = (a ** 5 + b ** 5 + c ** 5 + d ** 5) ** (1 / 5)
                if int(e) ** 5 == a ** 5 + b ** 5 + c ** 5 + d ** 5:
                    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'e =', int(e))
                    print('сумма =', a + b + c + d + int(e))
                    f = 1
                    break
            if f == 1:
                break
        if f == 1:
            break
    if f == 1:
        break