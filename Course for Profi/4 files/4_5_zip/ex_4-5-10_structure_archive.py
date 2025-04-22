'''
Структура архива 🌶️🌶️
Вам доступен архив desktop.zip, содержащий различные папки и файлы. Напишите программу, которая выводит
его файловую структуру и объем каждого файла.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести файловую структуру архива desktop.zip и объем каждого файла в несжатом виде. Так
как архив имеет собственную иерархию папок, каждый уровень вложенности должен быть выделен двумя пробелами.

Примечание 1. Вывод на примере архива test.zip из конспекта:

test
  Картинки
    1.jpg 88 KB
    avatar.png 19 KB
    certificate.png 43 KB
    py.png 33 KB
    World_Time_Zones_Map.png 2 MB
    Снимок экрана.png 11 KB
  Неравенства.djvu 5 MB
  Программы
    image_util.py 5 KB
    sort.py 61 B
  Разные файлы
    astros.json 505 B
Примечание 2. Объем файла записывается в самых крупных единицах измерения с округлением до целых.

Примечание 3. Значения единиц измерения такие же, какие приняты в информатике:

1 KB = 1024 B
1 MB = 1024 KB
1 GB = 1024 MB
Примечание 4. Указанный архив доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/547172/desktop.zip
https://stepik.org/media/attachments/lesson/547172/clue_archive_structure.txt
'''

from zipfile import ZipFile


def size_to_large(size):
    '''
    Функция принимает размер файла в байтах и возвращает строку в самых крупных единицах измерения
    с округлением до целых

    Единицы измерения:
    1 KB (Kilobyte) = 1,024 Bytes
    1 MB (Megabyte) = 1024 KB = 1,048,576 Bytes
    1 GB (Gigabyte) = 1024 MB = 1,048,576 KB = 1,073,741,824 Bytes
    1 TB (Terabyte) = 1024 GB = 1,048,576 MB = 8,388,608 KB = 1,099,511,627,776 Bytes
    1 PB (Petabyte) = 1024 TB = 1,048,576 GB = 1,073,741,824 MB = 1,099,511,627,776 KB = 1,125,899,906,842,624 Bytes
    1 EB (Exabyte) = 1024 PB = 1,048,576 TB = 1,073,741,824 GB = 1,099,511,627,776 MB = 1,125,899,906,842,624 KB = 1,152,921,504,606,846,976 Bytes
    1 ZB (ZettaByte) = 1024 EB = 1,048,576 PB = 1,073,741,824 TB = 1,099,511,627,776 GB = 1,125,899,906,842,624 MB = 1,152,921,504,606,846,976 KB = 1,180,591,620,717,411,303,424 Bytes
    1 YB (Yottabyte) = 1,000 ZB = 1,048,576 EB = 1,073,741,824 PB = 1,099,511,627,776 TBz = 1,125,899,906,842,624 GB = 1,152,921,504,606,846,976 MB = 1,180,591,620,717,411,303,424 KB = 1,208,925,819,614,629,174,706,176 Bytes
    '''

    measure = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
    count = 0
    while size >= 1024:
        size /= 1024
        count += 1
    return f'{round(size)} {measure[count]}'


with ZipFile('desktop.zip') as zip_file:
    data = zip_file.infolist()
    for file in data:
        source_name = file.filename
        indent_ = '  '
        if file.is_dir():
            spaces = (source_name.count('/') - 1) * indent_
            new_name = source_name.split('/')[-2]
            print(spaces + new_name)
        else:
            spaces = source_name.count('/') * indent_
            new_name = file.filename.split('/')[-1]
            print(f'{spaces + new_name} {size_to_large(file.file_size)}')