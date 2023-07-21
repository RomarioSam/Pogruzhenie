# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json,
# csv и pickle. Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория. Для файлов сохраните его размер в байтах,
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
# Пример:
# test/users/names.txt
# Результат в json для names.txt:
# {
# "name": names.txt
# "parent": users,         ужасный пример
# "type": "file"
# }


import os
import json
import csv
import pickle
import sys

xxx = os.getcwd()
os.chdir('..')
sys.path.append(os.getcwd())
os.chdir(xxx)
# from Rabota_s_failami import task6 # раскоментировать для создания файлов в папке new_dir и директорий в ней
os.chdir(xxx)


OUR_WAY = 'new_dir'
new_dict = {}
N = 1


def directories(dir_):
    if dir_ not in os.listdir():
        os.mkdir(dir_)
    os.chdir(dir_)
    global N
    for file in os.listdir():
        if '.' in file:
            new_dict[file] = {}
            new_dict[file]['parent'] = dir_
            new_dict[file]['type'] = 'file'
            new_dict[file]['size'] = f'{os.path.getsize(file)} bytes'
        else:
            directories(file)
            os.chdir('..')
            total_size = 0
            for root, dirs, files in os.walk(file):
                for f in files:
                    file_path = os.path.join(root, f)
                    total_size += os.path.getsize(file_path)
            if file in new_dict:
                file += f'00{N}'
                N += 1
            new_dict[file] = {}
            new_dict[file]['parent'] = dir_
            new_dict[file]['type'] = 'directory'
            new_dict[file]['size'] = f'{total_size} bytes'


directories(OUR_WAY)
os.chdir('..')
x = 1
for key, value in new_dict.items():  # вывод в консоль
    print(x, key, value)
    x += 1

with (
    open('taskDZ1.json', 'w', encoding='utf-8') as f1,
    open('taskDZ1.csv', 'w', encoding='utf-8', newline='') as f2,
    open('taskDZ1.pickle', 'wb') as f3
):
    json.dump(new_dict, f1, indent=4)
    www = csv.writer(f2, dialect='excel-tab')
    www.writerow(['name', 'parent', 'type', 'size'])
    for key, value in new_dict.items():
        www.writerow([key, value['parent'], value['type'], value['size']])
    pickle.dump(new_dict, f3)
