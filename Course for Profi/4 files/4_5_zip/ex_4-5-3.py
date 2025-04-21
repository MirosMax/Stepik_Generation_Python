'''
Наилучший показатель
Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит
название файла из этого архива, который имеет наилучший показатель степени сжатия.

Примечание 1. Если файл находится в папке, вывести следует только название без пути.

Примечание 2. Гарантируется, что в исходном архиве только один файл имеет наилучший показатель степени сжатия.

Примечание 3. Указанный архив доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/547172/workbook.zip
https://stepik.org/media/attachments/lesson/547172/clue_coef.txt
'''

from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    ratio_compress = 1
    best_file = 0
    for file in zip_file.infolist():
        if not file.is_dir():
            temp_ratio = file.compress_size / file.file_size
            if temp_ratio < ratio_compress:
                ratio_compress = temp_ratio
                best_file = file.filename
    print(best_file.split('/')[-1])