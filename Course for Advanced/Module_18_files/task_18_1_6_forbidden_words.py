'''
Forbidden words 🤬🌶️

На вход программе подается строка текста с именем текстового файла. Напишите программу, выводящую на экран содержимое
этого файла, но с заменой всех запрещенных слов звездочками * (количество звездочек равно количеству букв в слове).

Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt. Гарантируется, что все
слова в этом файле записаны в нижнем регистре.

Формат входных данных
На вход программе подается строка текста с именем существующего текстового файла, в котором необходимо заменить
запрещенные слова звездочками.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание 1. Ваша программа должна заменить запрещенные слова, где бы они ни встречались, даже если они встречаются
в середине другого слова.

Примечание 2. Программа должна заменять запрещенные слова независимо от их регистра. Например, если файл
forbidden_words.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и подобные должны быть заменены
на ****.

Примечание 4. Файл forbidden_words.txt и файлы ввода (data.txt, stepik.txt и beegeek.txt) лежат рядом с программой.
'''


with (open(input(), 'r', encoding='utf-8') as input_file,
      open('forbidden_words.txt', 'r', encoding='utf-8') as forbidden_file):
    forbidden_words = [s.strip() for s in forbidden_file.read().split()]
    text_origin = input_file.read()
    text_lower = text_origin.lower()
    for word in forbidden_words:
        if word in text_lower:
            hidden_word = len(word) * '*'
            count_word = text_lower.count(word)
            index_word = text_lower.find(word)
            for _ in range(count_word):
                text_origin = text_origin[:index_word] + hidden_word + text_origin[index_word + len(word):]
                index_word = text_lower.find(word, index_word + len(word))

    print(text_origin)