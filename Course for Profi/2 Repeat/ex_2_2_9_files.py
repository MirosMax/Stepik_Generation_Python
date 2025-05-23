'''
Файлы в файле 🌶️🌶️
Вам доступен текстовый файл files.txt, содержащий информацию о файлах. Каждая строка файла содержит три значения,
разделенные символом пробела — имя файла, его размер (целое число) и единицы измерения:

cant-help-myself.mp3 7 MB
keep-yourself-alive.mp3 6 MB
bones.mp3 5 MB
...

Напишите программу, которая группирует данные файлы по расширению, определяя общий объем файлов каждой группы, и
выводит полученные группы файлов, указывая для каждой ее общий объем. Группы должны быть расположены в лексикографическом порядке названий расширений, файлы в группах — в лексикографическом порядке их имен.

Примечание 1. Например, если бы файл files.txt имел вид:

input.txt 3000 B
scratch.zip 300 MB
output.txt 1 KB
temp.txt 4 KB
boy.bmp 2000 KB
mario.bmp 1 MB
data.zip 900 MB

то программа должна была бы вывести:

boy.bmp
mario.bmp
----------
Summary: 3 MB

input.txt
output.txt
temp.txt
----------
Summary: 8 KB

data.zip
scratch.zip
----------
Summary: 1 GB
где Summary — общий объем файлов группы.

Примечание 2. Гарантируется, что все имена файлов содержат расширение.

Примечание 3. Общий объем файлов группы записывается в самых крупных (максимально возможных) единицах измерения с
округлением до целых. Другими словами, сначала следует определить суммарный объем всех файлов группы, скажем, в байтах,
а затем перевести полученное значение в самые крупные (максимально возможные) единицы измерения. Примеры перевода:
1023 B -> 1023 B
1300 B -> 1 KB
1900 B -> 2 KB

Примечание 4. Значения единиц измерения такие же, какие приняты в информатике:
1 KB = 1024 B
1 MB = 1024 KB
1 GB = 1024 MB

Примечание 5. Указанный файл доступен по ссылке https://stepik.org/media/attachments/lesson/569749/files.txt.
Ответ на задачу доступен по ссылке https://stepik.org/media/attachments/lesson/569749/clue.txt.

Примечание 6. При открытии файла используйте явное указание кодировки UTF-8.
'''


def size_to_large(size):
    measure = ['B', 'KB', 'MB', 'GB']
    count = 0
    while size > 1024:
        size /= 1024
        count += 1
    return f'{round(size)} {measure[count]}'


with open('files.txt', 'r', encoding='UTF-8') as files:
    data = {}
    for file in files:
        name, size, measure = file.split()
        size = int(size)
        ext = name.split('.')[1]
        data[ext] = data.setdefault(ext, {'names': [], 'size': 0})
        data[ext]['names'].append(name)

        # Перевод размера файла в байты
        if measure == 'GB':
            size *= 1024 ** 3
        elif measure == 'MB':
            size *= 1024 ** 2
        elif measure == 'KB':
            size *= 1024

        data[ext]['size'] += size

for ext in sorted(data.keys()):
    print(*sorted(data[ext]['names']), sep='\n')
    print('----------')
    print(f'Summary: {size_to_large(data[ext]['size'])}\n')

