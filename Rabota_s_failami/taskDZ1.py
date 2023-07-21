# Напишите функцию группового переименования файлов.
# Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

NEW_NAME = 'silikon'
CURRENT_NUMBERS = 3
ORIGINAL_EXT = 'txt'
CHANGED_EXT = 'json'
RANGE = [3, 6]
import os


def rename_(current_name=NEW_NAME, cur_numbers=CURRENT_NUMBERS,
            orig_ext=ORIGINAL_EXT, chang_ext=CHANGED_EXT, rang=RANGE):
    n = poisk_n()

    def number_(n):
        if n < 10:
            return ''.join(['0' for _ in range(cur_numbers - 1)]) + str(n)
        if n < 100:
            return ''.join(['0' for _ in range(cur_numbers - 2)]) + str(n)

    for i in os.listdir():
        if os.path.isfile(i):
            x, y = i.split('.')
            if y == orig_ext:
                new_name = x[rang[0] - 1: rang[1]] + number_(n) + current_name + '.' + chang_ext
                os.rename(i, new_name)
                n += 1


def poisk_n():
    n = 1
    for i in os.listdir():
        if os.path.isfile(i):
            x, y = i.split('.')
            if y == CHANGED_EXT:
                new_n = ''
                for j in x:
                    if j in '0123456789':
                        new_n += j
                if int(new_n) >= n:
                    n = int(new_n) + 1
    return n


if 'new_dir' not in os.listdir():
    os.mkdir('new_dir')
os.chdir('new_dir')
rename_()
