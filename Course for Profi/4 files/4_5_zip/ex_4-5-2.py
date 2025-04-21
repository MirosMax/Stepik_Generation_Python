'''
Объем файлов
Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит
суммарный объем файлов этого архива в сжатом и не сжатом видах в байтах, в следующем формате:

Объем исходных файлов: <объем до сжатия> байт(а)
Объем сжатых файлов: <объем после сжатия> байт(а)
Примечание 1. Вывод на примере архива test.zip из конспекта:

Объем исходных файлов: 7810260 байт(а)
Объем сжатых файлов: 7798267 байт(а)
Примечание 2. Указанный архив доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/547172/workbook.zip
https://stepik.org/media/attachments/lesson/547172/clue_volumes.txt
'''

from zipfile import ZipFile
from functools import reduce


with ZipFile('workbook.zip') as zip_file:
    # size_origin = 0
    # size_compress = 0
    # for file in zip_file.infolist():
    #     if not file.is_dir():
    #         size_origin += file.file_size
    #         size_compress += file.compress_size
    files = zip_file.infolist()
    size_origin = reduce(lambda a, b: a + b.file_size, files, 0)
    size_compress = reduce(lambda a, b: a + b.compress_size, files, 0)

    print(f'''Объем исходных файлов: {size_origin} байт(а)
Объем сжатых файлов: {size_compress} байт(а)''')