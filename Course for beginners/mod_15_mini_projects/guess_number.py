import random

def is_valid(user_num):
    if user_num.isdigit() and left_limit <= int(user_num) <= right_limit:
        return True
    else:
        return False


print('Добро пожаловать в числовую угадайку!')
print()
print('Я загадаю ЦЕЛОЕ число, а вы попробуете отгадать. В каких пределах мне загадать число?')
left_limit = int(input('Укажите нижнюю границу: '))
right_limit = int(input('Укажите верхнюю границу: '))

while right_limit <= left_limit:
    right_limit = int(input('Верхняя граница должны быть больше нижней. Укажите верхнюю границу заново: '))

random_num = random.randint(left_limit, right_limit)
print()
print(f'Я загадал целое число в промежутке от {left_limit} до {right_limit} (включительно)!')

count_try = 0
while True:
    print()
    user_num = input('Как вы думаете, какое это число? ')
    if not is_valid(user_num):
        print(f'А может быть все-таки введем целое число от {left_limit} до {right_limit}?')
        continue
    user_num = int(user_num)
    count_try += 1
    if user_num == random_num:
        print()
        print('**********************//////!!!!!!**********************')
        print(f'Вы угадали, поздравляю!!! Я загадывал именно число {random_num}.')
        print(f'Вам потребовалось {count_try} попыток.')
        break
    elif user_num < random_num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        continue
    elif user_num > random_num:
        print('Ваше число больше загаданного, попробуйте еще разок')
        continue

print('________________________________________________________')
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
