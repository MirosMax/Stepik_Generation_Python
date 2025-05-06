'''
Функция print_bar_chart()
Реализуйте функцию print_bar_chart(), которая принимает два аргумента в следующем порядке:

data — строка или список строк
mark — одиночный символ
Функция должна определять:

сколько раз встречается каждый символ в строке, если data является строкой
сколько раз встречается каждая строка в списке, если data является списком
Затем функция должна выводить результат в виде столбчатой диаграммы, указывая каждый символ (строку) и его
количество. Количество отображается как повторение символа mark соответствующее число раз, например, если
mark='+', то количество, равное четырем, будет отображено как ++++. Символы (строки) в диаграмме должны быть
расположены в порядке уменьшения количества, при равных количествах — в своем исходном порядке, каждая на
отдельной строке, в следующем формате:

<символ или строка> |<количество>
Примечание 1. Обратите внимание на второй тест, функция должна добавлять нужное количество пробелов, если
строка имеет меньшую длину, чем другие.

Примечание 2. Программа должна учитывать регистр. То есть, например, строки Python и python считаются
различными.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию
print_bar_chart(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами https://stepik.org/media/attachments/lesson/635441/tests_2609489.zip
GitHub https://github.com/python-generation/Professional/tree/main/Module_6/Module_6.8/Module_6.8.20
Sample Input 1:

print_bar_chart('beegeek', '+')
Sample Output 1:

e |++++
b |+
g |+
k |+
Sample Input 2:

languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']

print_bar_chart(languages, '#')
Sample Output 2:

java      |####
C++       |###
pascal    |##
python    |#
assembler |#
C         |#
'''

from collections import Counter


def print_bar_chart(data, mark):
    data_count = Counter(data)
    space_count = len(max(data, key=len)) + 1
    for item, count in data_count.most_common():
        print(f'{item.ljust(space_count)}|{mark * count}')


print_bar_chart('beegeek', '+')
languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']

print_bar_chart(languages, '#')