a, b = int(input()), int(input())

for i in range(b, 1, -1):
    if b % i == 0:
        if a % i == 0:
            print('соотношение сторон', a / i, ':', b / i)
            break