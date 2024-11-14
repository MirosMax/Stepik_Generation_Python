def chunked(s, n):
    result = []

    while len(s) > 0:
        result.append(s[:n])
        del s[:n]

    return result

s = input().split()
n = int(input())

print(chunked(s, n))
