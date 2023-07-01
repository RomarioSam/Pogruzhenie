# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента.
# (речь идет про **kwargs)

abc = 1
def dick(**lalala):
    new_lalala = {}
    for k, v in lalala.items():
        new_lalala[v] = k
    return new_lalala


print(dick(bmw='x5', mers=600, abc='edf'))
