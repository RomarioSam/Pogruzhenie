# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple. Каждый объект хранит:
# имя файла без расширения или название каталога,
# расширение, если это файл,
# флаг каталога,
# название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.


import logging
from collections import namedtuple
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('wey', nargs='*')
way = ' '.join(parser.parse_args().wey)
os.chdir(way)
Obje = namedtuple('Obje', 'name exp father', defaults=['none', 'none', 'none'])
objs = []
FORMAT = '{levelname:<8} {asctime}    {name}'
loguna = logging.basicConfig(filename='loguna.log', filemode='w', encoding='utf-8', level=logging.INFO,
                             format=FORMAT, style ='{')
def save_obj():
    for i in os.listdir():
        if os.path.isfile(i):
            if '.' in i:
                objs.append(Obje(name=i.split('.')[0], exp=i.split('.')[1], father=os.getcwd().split('\\')[-1]))
            else:
                objs.append(Obje(name=i, father=os.getcwd().split('\\')[-1]))
            logging.getLogger(name=f'{objs[-1]}').info("здрасьте")
        if os.path.isdir(i):
            objs.append(Obje(name=i, father=os.getcwd().split('\\')[-1]))
            logging.getLogger(name=f'{objs[-1]}').info('здрасьте')
            os.chdir(i)
            save_obj()
            os.chdir('..')

print(os.getcwd())
save_obj()
for i in objs:
    print(i)
print(os.getcwd())




# FORMAT = '{levelname:<8}  {asctime}   {name}   {lineno:03d}   {funcName}   {created}   {msg}'
# lo = logging.basicConfig(filename='logilogi.log', filemode='w', encoding='utf-8', level=logging.NOTSET,
#                          format=FORMAT, style='{')
#
# logger = logging.getLogger(name='gggggg')
# logger.warning('Внимание внимание')
#
#
# Point = namedtuple('Point', 'a b c', defaults=[0, 0, 0])
# p1 = Point()
# p1 = p1._replace(a=p1.b+6)
# p2 = p1._replace(a=3, c=9)
# print(p1, p2, sep='\n')


# parser = argparse.ArgumentParser(description='hehehehehehehe')
# parser.add_argument('numders', metavar='SSS', type=float, nargs='*', help='lalalalalalalalala')
#
# parser.add_argument('-x', action='store_const', const=30)
# parser.add_argument('-y', action='store_true')
# parser.add_argument('-z', action='append')
# parser.add_argument('-a', action='append_const', const=15, dest='pykk')
# args = parser.parse_args()
# print(args)
# python