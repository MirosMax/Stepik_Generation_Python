'''
Вам доступен именованный кортеж Game. Дополните приведенный ниже код, чтобы он объявлял тип ExtendedGame
именованного кортежа, имеющего те же поля, что и Game, а также два дополнительных поля — release_date и price.

Примечание. Программа ничего не должна выводить.
'''

from collections import namedtuple

Game = namedtuple('Game', 'name developer publisher')

ExtendedGame = namedtuple('ExtendedGame', 'name developer publisher release_date price')