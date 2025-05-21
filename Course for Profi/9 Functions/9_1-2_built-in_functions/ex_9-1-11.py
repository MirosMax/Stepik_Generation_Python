'''
Необычная сортировка 🌶️
Дана строка, содержащая латинские буквы и цифры. Напишите программу, которая сортирует символы в строке согласно
следующим правилам:

все отсортированные строчные буквы стоят перед заглавными буквами
все отсортированные заглавные буквы стоят перед цифрами
все отсортированные нечетные цифры стоят перед отсортированными четными
Формат входных данных
На вход программе подается строка, содержащая латинские буквы и цифры.

Формат выходных данных
Программа должна расположить символы в строке в соответствии с условием задачи и вывести полученный результат.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами https://stepik.org/media/attachments/lesson/640035/tests_2657880.zip
GitHub https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.1/Module_9.1.16
Sample Input 1:

Sorting1234
Sample Output 1:

ginortS1324
Sample Input 2:

n0tEast3rEgg
Sample Output 2:

aggnrsttEE30
Sample Input 3:

3DYrz34UXl
Sample Output 3:

lrzDUXY334
'''

data = input()

al_upper = []
al_lower = []
dig_odd = []
dig_even = []

for i in data:
    if i.isalpha():
        if i.isupper():
            al_upper.append(i)
        elif i.islower():
            al_lower.append(i)
    else:
        num = int(i)
        if num % 2 == 0:
            dig_even.append(num)
        else:
            dig_odd.append(num)

new_data = map(sorted, (al_lower, al_upper, dig_odd, dig_even))
for i in new_data:
    print(*i, sep='', end='')
