# Создайте функцию для сортировки файлов по директориям:
# видео, изображения, текст и т.п. Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os


def unpacking(direct):           # вытаскиваем все файлы из всех папок в корень, в папку new_dir
    for i in os.listdir():
        if '.' not in i:
            os.chdir(i)
            unpacking(direct)
        if '.' in i:
            os.replace(f"{os.getcwd()}/{i}", f"{direct}/{i}")
    os.chdir('..')


def sort_():                     # раскидываем файлы по новым папкам с названиями их расширений
    for i in os.listdir():
        if '.' in i:
            zzz = f'{(i.split("."))[1]}_folder'
            if zzz not in os.listdir():
                os.mkdir(zzz)
            os.replace(i, f'{zzz}/{i}')


if 'new_dir' not in os.listdir():
    os.mkdir('new_dir')
os.chdir('new_dir')
unpacking(os.getcwd())
os.chdir('new_dir')
sort_()
