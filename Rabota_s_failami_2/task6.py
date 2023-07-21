# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

import os
import pickle
import json
import csv
def pickle_transformer(pickle_file_name):
    name, _ = os.path.splitext(pickle_file_name)
    with (
        open(pickle_file_name, 'rb') as file,
        open('task_6_restored_' + name + '.csv', 'w', encoding='utf-8') as w_file
    ):
        data = pickle.load(file)

        j_data = json.loads(data)
        field_names = j_data[0].keys()
        writer = csv.DictWriter(w_file, fieldnames=field_names, dialect='excel', quoting=csv.QUOTE_ALL)
        for row in j_data:
            writer.writerow(row)



pickle_transformer('out_file_4.pickle')