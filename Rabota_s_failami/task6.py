# Дорабатываем функции из предыдущих задач.
# Генерируйте файлы в указанную директорию - отдельный параметр функции.
# Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# Существующие файла не должны удаляться/изменяться в случае совпадения имён.
import os
import sys

sys.path.append(os.getcwd())
from Rabota_s_failami.task4 import fails


def fails3(str1):
    x = str1.split()
    for i in range(0, len(x) - 2, 3):
        a = '.' + x[i]
        b = int(x[i + 1])
        c = x[i + 2]
        fails(a, b, c)


fails3(input('\nВведите расширения, количество файлов и директории для них через пробел. \n' \
             'Например: txt 3 text/podtext py 5 pythonDZ/lalala ... : \n'))
