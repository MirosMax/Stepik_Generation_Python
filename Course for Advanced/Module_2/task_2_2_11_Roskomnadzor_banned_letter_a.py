word = input() + ' запретил букву'
letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
           'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

while len(word) > 0:
    if letters[0] in word:
        print(word + ' ' + letters[0])
        word_list = list(word)
        while letters[0] in word_list:
            word_list.remove(letters[0])
        word = ''.join(word_list).strip()
        del letters[0]
        while '  ' in word:  # удаляем двойные пробелы
            index_spaces = word.index('  ')
            word = word[:index_spaces] + word[index_spaces + 1:]
    else:
        del letters[0]

