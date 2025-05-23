'''
Бесплатные курсы берут свое 😭
Тимур продает книги по математике за 1—11 класс. У него есть список, в котором указаны все книги, имеющиеся
в наличии. К Тимуру приходят n покупателей, называют номер класса, за который они хотят приобрести книгу,
и сумму, которую они готовы заплатить, и если книга есть в наличии, Тимур ее продает.

Напишите программу, которая вычисляет общую сумму денег, которую Тимур заработает на продаже книг.

Формат входных данных
На вход программе в первой строке подается последовательность чисел, разделенных пробелом, представляющих
набор книг, которые имеются в наличии. Каждое число последовательности — книга за указанный класс, например,
последовательность 1 1 4 представляет набор из двух книг за первый класс и одной книги за четвертый класс.
Вторая строка содержит число n — количество покупателей. В последующих n строках вводятся два числа,
разделенные пробелом, где первое число является номером класса, второе — суммой, предлагаемой покупателем.

Формат выходных данных
Программа должна вывести единственное число — общую сумму денег, которую заработал Тимур.

Примечание. Рассмотрим первый тест. В первой строке указан список книг, которые есть в наличии:

2 книги за 1-й класс
1 книга за 11-й класс
3 книги за 9-й класс
2 книги за 5-й класс
1 книга за 7-й класс

В следующей строке указано число
7 — количество покупателей. Последующие 7 строк содержат номер класса и некоторую сумму:

первый покупатель приобретает книгу за 1-й класс за 300р
второй покупатель приобретает книгу за 1-й класс за 250р
третий покупатель приобретает книгу за 11-й класс за 400р
книг за 1-й класс больше нет в наличии, поэтому покупка невозможна
пятый покупатель приобретает книгу за 7-й класс за 200р
шестой покупатель приобретает книгу за 9-й класс за 400р
книг за 7-й класс больше нет в наличии, поэтому покупка невозможна
Итого Тимур заработал 300+250+400+200+400=1550р.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами https://stepik.org/media/attachments/lesson/635441/tests_2611031.zip
GitHub https://github.com/python-generation/Professional/tree/main/Module_6/Module_6.8/Module_6.8.22
Sample Input 1:

1 1 11 9 5 5 7 9 9
7
1 300
1 250
11 400
1 300
7 200
9 400
7 250
Sample Output 1:

1550
Sample Input 2:

1 1 2 3 4 5
3
9 1000
10 2000
11 1500
Sample Output 2:

0
'''

from collections import Counter

catalog = Counter(input().split())
total = 0

for _ in range(int(input())):
    book, price = input().split()
    price = int(price)
    if catalog[book]:
        total += price
        catalog[book] -= 1

print(total)