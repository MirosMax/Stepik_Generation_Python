s = 'w w w o r l d g g g g r e a t t e c c h e m g g p w w'
s = s.split()

result = []

nest_s = [s[0]]
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        nest_s += s[i]
    else:
        result.append(nest_s)
        nest_s = [s[i]]
    if i == len(s) - 1:
        result.append(nest_s)


print(result)
