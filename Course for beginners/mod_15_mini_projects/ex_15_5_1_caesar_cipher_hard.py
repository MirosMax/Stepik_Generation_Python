'''На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова. Каждое слово
строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова). Строчные буквы при этом
остаются строчными, а прописные – прописными. Гарантируется, что между различными словами присутствует один пробел.

Формат входных данных
На вход программе подается строка текста на английском языке.

Формат выходных данных
Программа должна вывести зашифрованный текст в соответствии с условием задачи.

Примечание. Символы, не являющиеся английскими буквами, не изменяются.'''


def counts_shift():
    'Функция подсчитывает сдвиг по длине слова. Возвращает сдвиг и слово без шифрования'
    global text
    crypt_temp = ''
    count_shift = 0
    for char in text:  # подсчет сдвига
        if char.isalpha():
            count_shift += 1
        else:
            break
    crypt_temp += ''.join(text[:count_shift])  # превращаем список в строку из нужного слова
    del text[:count_shift]  # удаляем символы найденного слова из исходного текста
    return crypt_temp, count_shift


def find_index(symbol, letters, shift):
    'Функция ищет индекс исходного символа и возвращает зашифрованный символ'
    index_old_alpha = letters.index(symbol)
    index_new_alpha = index_old_alpha + shift
    if index_new_alpha > (len(letters) - 1):
        index_new_alpha -= len(letters)
    elif index_new_alpha < 0:
        index_new_alpha += len(letters)
    return letters[index_new_alpha]


text = list(input())  # преобразуем в список, для удобства удаления элементов
decryption = ''

en_lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
en_uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while len(text) > 0:
    if text[0].isalpha():
        # если буква, то запускаем подсчет сдвига, шифруем слово, и удаляем его из исходного текста
        encrypt_temp, shift = counts_shift()
        for el in encrypt_temp:
            if el in en_lowercase_letters:
                decryption += find_index(el, en_lowercase_letters, shift)
            elif el in en_uppercase_letters:
                decryption += find_index(el, en_uppercase_letters, shift)
    else:
        # если символ, то добавляем к зашифрованному варианту без изменений и удаляем из исходного текста
        decryption += text[0]
        del text[0]

print(decryption)
