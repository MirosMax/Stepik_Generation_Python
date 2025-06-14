'''
Итератор CardDeck
Реализуйте класс CardDeck, порождающий итераторы, конструктор которого не принимает никаких аргументов.

Итератор класса CardDeck должен генерировать последовательность из 52 игральных карт, а после возбуждать исключение StopIteration. Каждая карта должна представлять собой строку в следующем формате:

<номинал> <масть>
Например, 7 пик, валет треф, дама бубен, король червей, туз пик.

Примечание 1. Карты, генерируемые итератором, должны располагаться сначала по величине номинала, затем масти.

Примечание 2. Старшинство мастей по возрастанию: пики, трефы, бубны, червы. Старшинство карт в масти по возрастанию: двойка, тройка, четверка, пятерка, шестерка, семерка, восьмерка, девятка, десятка, валет, дама, король, туз.

Примечание 3. Масти не требуют склонения и независимо от номинала должны сохранять следующее написание: пик, треф, бубен, червей.

Примечание 4. В тестирующую систему сдайте программу, содержащую только необходимый класс CardDeck.
'''

# 1 вариант
# class CardDeck():
#     def __init__(self):
#         self.index = -1
#         suits = ['пик', 'треф', 'бубен', 'червей']
#         nominals = list(range(2, 11)) + ['валет', 'дама', 'король', 'туз']
#         self.req = [(n, s) for s in suits for n in nominals]
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == 51:
#             raise StopIteration
#         else:
#             self.index += 1
#             return f'{self.req[self.index][0]} {self.req[self.index][1]}'


# 2 вариант (оптимальнее)
class CardDeck():
    def __init__(self):
        suits = ['пик', 'треф', 'бубен', 'червей']
        nominals = list(range(2, 11)) + ['валет', 'дама', 'король', 'туз']
        self.req = iter((n, s) for s in suits for n in nominals)

    def __iter__(self):
        return self

    def __next__(self):
        card = next(self.req)
        return f'{card[0]} {card[1]}'


# INPUT DATA:

# TEST_1:
cards = CardDeck()

print(next(cards))
print(next(cards))

# TEST_2:
cards = list(CardDeck())

print(cards[9])
print(cards[23])
print(cards[37])
print(cards[51])

# TEST_3:
cards = list(CardDeck())

print(cards)

# TEST_4:
cards1 = list(CardDeck())
cards2 = tuple(CardDeck())
cards3 = list(CardDeck())

print(cards1)
print(cards2)
print(cards3)

# TEST_5:
cards = list(CardDeck())

try:
    next(cards)
except:
    print('Error')