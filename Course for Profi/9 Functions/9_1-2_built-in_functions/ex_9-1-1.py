'''
Строчный алфавит
Напишите программу, которая выводит все строчные латинские буквы.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести все строчные латинские буквы от a до z, каждую на отдельной строке.

Примечание. В задаче удобно воспользоваться функциями ord() и chr().
'''

start = ord('a')
stop = ord('z')

for i in range(start, stop + 1):
    print(chr(i))