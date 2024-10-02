for a in range(1, 51):
    for b in range(1, 51):
        for c in range(1, 51):
            for d in range(1, 51):
                if a ** 3 + b ** 3 == c ** 3 + d ** 3 and a != b and b != c and c != d and a != c and a != d and b != d:
                    print(a ** 3 + b ** 3)