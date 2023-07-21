# Задача 3
# Напишите функцию, которая сохраняет созданный
# в прошлом задании файл в формате CSV.

import csv
import json


def in_csv():
    with open('task_2.json', 'r', encoding='utf-8') as f1:
        xxx = json.load(f1)
        print(xxx)
    with open('task_3.csv', 'w', encoding='utf-8') as f2:
        f2.write('Level, ID, Name')

        for lev, id_ in xxx.items():
            for id__ , names in id_.items():
                f2.write(f'\n{lev}, {id__}, {names}')




in_csv()