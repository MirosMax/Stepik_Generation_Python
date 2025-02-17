def print_matrix(*args):
    if len(args) == 1:
        n = m = args[0]
    else:
        n, m = args[0], args[1]

    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=' ')
        print()


horse = input()
x, y = horse[0], int(horse[1])

alpha = []
for i in range(8):
    alpha.append(chr(ord('a') + i))

x = alpha.index(x)

matrix = []
for i in range(8):
    temp = ['.'] * 8
    matrix.append(temp)

n_horse = 8 - y
m_horse = x
matrix[n_horse][m_horse] = 'N'

for i in range(1, 3):
    for j in range(1, 3):





print_matrix(8)