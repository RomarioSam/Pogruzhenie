# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.

import pickle
def reader_csv(csv_file_name):
    with open(csv_file_name, 'r', encoding='utf-8') as f:
        reader = f.read()
        return pickle.dumps(reader)


print(reader_csv('task_6_restored_out_file_4.csv'))