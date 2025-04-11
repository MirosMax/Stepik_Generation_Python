'''
Функция csv_columns()
Реализуйте функцию csv_columns(), которая принимает один аргумент:

filename — название csv файла, например, data.csv
Функция должна возвращать словарь, в котором ключом является название столбца файла filename, а значением —
список элементов этого столбца.

Примечание 1. Гарантируется, что в передаваемом в функцию файле разделителем является запятая, при этом
кавычки не используются.
Примечание 2. Гарантируется, что у передаваемого в функцию файла первая строка содержит названия столбцов.
Примечание 3. Например, если бы файл exam.csv имел вид:

name,grade
Timur,5
Arthur,4
Anri,5
то следующий вызов функции csv_columns():

csv_columns('exam.csv')
должен был бы вернуть:

{'name': ['Timur', 'Arthur', 'Anri'], 'grade': ['5', '4', '5']}
Примечание 4. Ключи в словаре, а также элементы в списках должны располагаться в своем исходном порядке.
Примечание 5. В тестирующую систему сдайте программу, содержащую только необходимую функцию csv_columns(), но
не код, вызывающий ее.
Примечание 6. Тестовые данные доступны по ссылкам:

Архив с тестами https://stepik.org/media/attachments/lesson/518491/tests_3072469.zip
GitHub https://github.com/python-generation/Professional/tree/main/Module_4/Module_4.2/Module_4.2.15
'''

import csv


def csv_columns(filename):
    with open(filename, 'r', encoding='utf-8') as csv_file:
        data = csv.DictReader(csv_file)
        col_names = data.fieldnames
        result = {}
        for row in data:
            for name in col_names:
                result[name] = result.get(name, []) + [row[name]]

    return result
