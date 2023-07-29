# Напишите следующие функции:
# * Нахождение корней квадратного уравнения
# * Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# * Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# * Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import json
from random import randint as rnd


def generate_csv():
    with open('taskDZ1.csv', 'w') as f1:
        lalala = csv.writer(f1, dialect='excel')
        for _ in range(rnd(100, 1000)):
            lalala.writerow((rnd(-100, 100), rnd(-100, 100), rnd(-100, 100)))

generate_csv()

def deco1(func):
    def wrapper(*args):
        listik = []
        with open('taskDZ1.csv', 'r') as f2:
            lala = csv.reader(f2, quoting=csv.QUOTE_NONNUMERIC)
            for i in lala:
                if i != []:
                    listik.append(func(*i))
            return listik
    return wrapper

def deco2(func):
    def wrapper(*args):
        with open('taskDZ1.json', 'w', encoding='utf-8') as f3:
            json.dump(func(*args), f3, ensure_ascii=False, indent=2)
    return wrapper

@deco2
@deco1
def square(*args):
    a, b, c = args
    d = b*b - 4*a*c
    if d < 0:
        return 'нет корней'
    x1 = (-b + d**0.5)/2*a
    x2 = (-b - d**0.5)/2*a
    return x1, x2

square()



