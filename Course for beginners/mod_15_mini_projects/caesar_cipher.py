'''
Шифр Цезаря

Описание проекта: требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом
Цезаря.

Примечание 1. Считайте, что в русском языке 32 буквы (буква ё отсутствует).
Примечание 2. Неалфавитные символы — знаки препинания, пробелы, цифры — не меняются.
Примечание 3. Сохраните регистр символов. Например, текст: "Умом Россию не понять" при сдвиге на одну позицию вправо
будет преобразован в: "Фнпн Спттйя ож рпоауэ".

Алгоритм:

'''
def find_index(symbol, letters):
    index_old_alpha = letters.index(symbol)
    global shift
    index_new_alpha = index_old_alpha + shift
    if index_new_alpha > (len(letters) - 1):
        index_new_alpha -= len(letters)
    elif index_new_alpha < 0:
        index_new_alpha += len(letters)
    return letters[index_new_alpha]


print('Здравствуйте! Я помогу вам зашифровать или расшифровать шифр Цезаря')
print('-------------------------------------------------------------------\n')
text = input('Введите текст для шифровки/дешифровки: ')
shift = int(input('Введите сдвиг символов (вправо-положительный, влево-отрицательный): '))

en_lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
en_uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ru_lowercase_letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
ru_uppercase_letters = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

# функционал Шифрования
encrypted_text = ''
for i in range(len(text)):
    if text[i] in en_lowercase_letters:
        encrypted_text += find_index(text[i], en_lowercase_letters)
    elif text[i] in en_uppercase_letters:
        encrypted_text += find_index(text[i], en_uppercase_letters)
    elif text[i] in ru_lowercase_letters:
        encrypted_text += find_index(text[i], ru_lowercase_letters)
    elif text[i] in ru_uppercase_letters:
        encrypted_text += find_index(text[i], ru_uppercase_letters)
    else:
        encrypted_text += text[i]
print('\nРезультат:', encrypted_text)
