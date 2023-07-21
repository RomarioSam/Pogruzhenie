# Вспоминаем задачу 3 из прошлого семинара.
# Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки.

import json


def new_file(old_file):
    with open(f'{old_file}', 'r', encoding='utf-8') as f1:
        y = dict(map(lambda x: tuple(x.split()), f1.read().split('\n')))
    with open('new_file_task1.json', 'w', encoding='utf-8') as f2:
        json.dump(y , f2)


new_file('old_file_Seminar7_task3.txt')

