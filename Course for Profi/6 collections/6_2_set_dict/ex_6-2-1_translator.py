'''
Я и сам своего рода переводчик
Дана строка соответствия латинскому алфавиту: первый символ строки соответствует букве a, второй — b, третий — c, и так далее. Каждый символ соответствует как заглавной, так и строчной буквам. Количество символов в строке совпадает с количеством букв в латинском алфавите.

Напишите программу, которая с помощью данной строки переводит заданный текст.

Формат входных данных
На вход программе в первой строке подается строка соответствия латинскому алфавиту, в следующей — текст, требующий перевода.

Формат выходных данных
Программа должна с помощью данной строки соответствия латинскому алфавиту перевести введенный текст и вывести полученный результат.

Примечание 1. Программа должна игнорировать все символы, не являющиеся латинскими буквами.

Примечание 2. Составить словарь соответствия можно с помощью строкового метода maketrans(), подробнее о
котором рассказывается по ссылке
https://docs-python.ru/tutorial/operatsii-tekstovymi-strokami-str-python/metod-str-maketrans/

Примечание 3. Тестовые данные доступны по ссылкам:
Архив с тестами https://stepik.org/media/attachments/lesson/631917/tests_3079498.zip
GitHub https://github.com/python-generation/Professional/tree/main/Module_6/Module_6.2/Module_6.2.17
'''

import string

trans_table = str.maketrans(string.ascii_lowercase, input())
text = input().lower()

print(text.translate(trans_table))