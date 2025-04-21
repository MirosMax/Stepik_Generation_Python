'''
Количество файлов
Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит
единственное число — количество файлов в этом архиве.

Примечание 1. Обратите внимание, что папка не считается файлом.

Примечание 2. Указанный архив доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/547172/workbook.zip
https://stepik.org/media/attachments/lesson/547172/clue_files_num.txt
'''
from zipfile import ZipFile
from functools import reduce


with ZipFile('workbook.zip') as zip_file:
    # counter = 0
    # for file in zip_file.infolist():
    #     if not file.is_dir():
    #         counter += 1
    counter = reduce(lambda a, b: a + (not b.is_dir()), zip_file.infolist(), 0)
    print(counter)
