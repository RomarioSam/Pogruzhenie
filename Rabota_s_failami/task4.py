# Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры: расширение
#
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.

HEIGH_MIN = 6
HEIGH_MAX = 30
BYTE_MIN = 256
BYTE_MAX = 4096
FILE_COUNT = 3  # 42

from random import randint as rin
import os


def fails(ext='.txt', count=FILE_COUNT, direk=''):
    for _ in range(count):                                                    # цикл с указанным количеством файлов
        lenght = rin(HEIGH_MIN, HEIGH_MAX)                                    # рандомное кол-во символов в названии
        rbytes = rin(BYTE_MIN, BYTE_MAX)                                      # рамдомное кол-во байт
        if direk != '':                                                       # если была указана другая директория
            start_dir = os.getcwd()                                           # то запоминаем стартовый путь
            examination(direk)             #  и заходим в проверку, проверяем, есть ли такая папка, если нет, то создаем
        name_ = ''.join([chr(rin(97, 122)) for _ in range(lenght)]) + ext     # генерация названия файла
        with open(f'{name_}', 'w') as file1:                                  # создание файла
            file1.write(''.join([chr(rin(97, 122)) for _ in range(rbytes)]))  #  забивание файла байтами
        if direk != '':                                                       #  проверка, чтобы вернуться
            os.chdir(start_dir)                                               #  в стартовую директорию



def examination(direk):
    if '/' in direk:                 # если из 6 задания указали директорию как путь
        x, y = direk.split('/', 1)   #  то берем в (х) первую папку, а остальное в (у)
        if x in os.listdir() and '/' in y:    #   если такая папка (х) уже есть а вторая часть (у) является путем
            os.chdir(x)              #    то заходим в эту папку (х)
            examination(y)           #    и рекурсия
        elif x in os.listdir():      #    если есть папка (х), а (у) не является путем, а является папкой
            os.chdir(x)              #    то заходим в папку (х)
            if y not in os.listdir():        #  если папки (у) нету
                os.mkdir(y)          #    то создаем ее
            os.chdir(y)              #    и заходим в (у)
            return                   #    и выходим из проверки
        else:
            os.makedirs(direk)       #    если папки (х) уже нету, а (у) еще путь или папка, то создаем дерево
            os.chdir(direk)          #    и заходим туда
    else:
        if direk not in os.listdir():       # если директория (direk) не путь, а просто папка
            os.mkdir(direk)          #        то создаем ее, если нету, и заходим
        os.chdir(direk)





if True: # __name__ == '__main__':
    if 'new_dir' not in os.listdir():
        os.mkdir('new_dir')
    os.chdir('new_dir')
