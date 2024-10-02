nickname = input()
flag = 'Incorrect'

if nickname[0] == '@' and 5 <= len(nickname) <= 15:
    if nickname[1:].isdigit():
        flag = 'Correct'
    elif nickname[1:].isalnum() and nickname[1:].islower():
        flag = 'Correct'


print(flag)