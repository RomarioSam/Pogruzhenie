# Напишите функцию, которая ищет json файлы
# в указанной директории и сохраняет
# их содержимое в виде одноимённых pickle файлов.

import os
import pickle

def search_files():
    files = list(file for file in os.listdir('.') if file.endswith('.json'))
    print(files)
    for file in files:
        name, _ = os.path.splitext(file)
        with (
            open(file, 'r') as r_file,
            open(name + '.pickle', 'wb') as w_file
        ):
            data = r_file.read()
            pickle.dump(data, w_file)


search_files()