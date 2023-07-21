# Прочитайте созданный в прошлом задании csv файл
# без использования csv.DictReader. Дополните id до
# 10 цифр незначащими нулями. В именах первую букву
# сделайте прописной. Добавьте поле хеш на основе имени
# и идентификатора. Получившиеся записи сохраните в json
# файл, где каждая строка csv файла представлена как
# отдельный json словарь. Имя исходного и конечного
# файлов передавайте как аргументы функции.
import csv
import json

def import_csv_in_json(csv_file, out_file):
    with open(csv_file, 'r', encoding='utf-8') as f1:
        data = list(map(lambda x: x.split(', '), f1.read().split('\n')))

    data[0].append('Hash')
    data[0][0], data[0][1] = data[0][1], data[0][0]
    for i in range(1, len(data)):
        data[i][0] = data[i][0].zfill(10)
        data[i][2] = data[i][2].capitalize()
        data[i].append(hash(data[i][0] + data[i][2]))
    print(data)
    data1 = [{'ID': u_id, 'Level': level, 'Name': uname, 'Hash': uhash} for u_id, level, uname, uhash in data]
    with open(out_file, 'w', encoding='utf-8') as res:
        json.dump(data1, res, indent=2)


import_csv_in_json('task_3.csv', 'out_file_4.json')