'''
Функция sourcetemplate()
Строка запроса (query string) — часть URL адреса, содержащая ключи и их значения. Она начинается после вопросительного знака и идет до конца адреса. Например:

https://beegeek.ru?name=timur     # строка запроса: name=timur
Если параметров в строке запроса несколько, то они отделяются символом амперсанда &:

https://beegeek.ru?name=timur&color=green     # строка запроса: name=timur&color=green
Реализуйте функцию sourcetemplate(), которая принимает один аргумент:

url — URL адрес
Функция sourcetemplate() должна возвращать функцию, которая принимает произвольное количество именованных аргументов и возвращает url адрес, объединенный со строкой запроса, сформированной из переданных аргументов. При вызове без аргументов она должна возвращать исходный url адрес без изменений.

Примечание 1. Параметры в строке запроса должны располагаться в лексикографическом порядке ключей.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию sourcetemplate(), но не код, вызывающий ее.

'''


def sourcetemplate(url):
    def metrics(**kwargs):
        if not kwargs:
            return url
        link_tail = []
        for k, v in kwargs.items():
            link_tail.append(f'{k}={v}')
        return url + '?' + '&'.join(sorted(link_tail))
    return metrics


url = 'https://all_for_comfort_life.com'
load = sourcetemplate(url)
print(load(smartphone='iPhone', notebook='huawei', sale=True))