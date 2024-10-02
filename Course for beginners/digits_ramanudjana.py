total = 0
for x in range(1, 51):
    for y in range(1, 51):
        for a in range(1, 51):
            for b in range(1, 51):
                if x == a or x == b or y == a or y == b:
                    continue
                z = x ** 3 + y ** 3
                k = a ** 3 + b ** 3
                if z == k and z > 1729:
                    total += 1
                    print(z, '=', x, '^3 +', y, '^3', '=', a, '^3 +', b, '^3')