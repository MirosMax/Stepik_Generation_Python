n = int(input())

for i in range(1, n + 1):
    text = input()
    if text == '' or text.isspace() == True:
        print(i, ': COMMENT SHOULD BE DELETED', sep='')
    else:
        print(i, ': ', text, sep='')