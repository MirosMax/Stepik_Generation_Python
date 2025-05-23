'''
Код Морзе

Код Морзе для представления цифр и букв использует тире и точки.
Напишите программу для кодирования текстового сообщения в соответствии с кодом Морзе.

Символ	Код	Символ	Код	Символ	Код	Символ	Код
A	.-	J	.---	S	...	1	.----
B	-...	K	-.-	T	-	2	..---
C	-.-.	L	.-..	U	..-	3	...--
D	-..	M	--	V	...-	4	....-
E	.	N	-.	W	.--	5	.....
F	..-.	O	---	X	-..-	6	-....
G	--.	P	.--.	Y	-.--	7	--...
H	....	Q	--.-	Z	--..	8	---..
I	..	R	.-.	0	-----	9	----.

Формат входных данных
На вход программе подается одна строка – текстовое сообщение.

Формат выходных данных
Программа должна вывести закодированное с помощью кода Морзе сообщение, оставляя пробел между каждым закодированным символом (последовательностью тире и точек).

Примечание 1. Ваша программа должна игнорировать любые символы, не перечисленные в таблице.
'''

letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = [
    '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
    '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--',
    '....-', '.....', '-....', '--...', '---..', '----.'
]

dict_morse = {}
for i in range(len(letters)):
    dict_morse[letters[i]] = morse[i]

text = input()

for sym in text:
    sym = sym.upper()
    if sym in dict_morse:
        print(dict_morse[sym], end=' ')
        continue
