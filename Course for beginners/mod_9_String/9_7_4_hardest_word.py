list_word = [input(), input(), input(), input()]
list_weigt = []

for c in list_word:
    weight = 0
    for a in c:
        weight += ord(a)

    list_weigt.append(weight)
index_max = list_weigt.index(max(list_weigt))

print(list_word[index_max])