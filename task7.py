# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце

import pprint as pp

ads = bmw = leksus = morfius = s = ntv = russia = bus = 1


def __names__(kwargs):
    kwargs2 = {}
    for k, v in kwargs.items():
        if k[-1:] == 's' and len(k) > 1:
            kwargs2[k[:-1]] = v
            kwargs[k] = None
    return kwargs2


pp.pprint(locals())
locals().update(__names__(locals()))
pp.pprint(locals())
print(russia, morfiu, morfius)
