# Напишите функцию, которая в бесконечном цикле запрашивает имя,
# личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.

import  json

def base_():
    try:
        while True:
            with open('task_2.json', 'r', encoding='utf-8') as f1:
                xxx = json.load(f1)
            mass_id = [j for i in xxx.values() for j in i]

            a, b, c = input('\nВведите Имя, ID, уровень доступа (от 1 до 7) через пробел: ').split()
            if int(c) > 7 or int(c) < 0:
                print('\nВведен несуществующий уровень доступа. Повторите попытку')
                base_()
                return
            if b in mass_id:
                print('\n Такой ID уже занят. Повторите попытку')
                base_()
                return
            if c not in xxx:
                xxx[c] = {b: a}
            elif c in xxx:
                xxx[c][b] = a
            print(xxx)
            with open('task_2.json', 'w', encoding='utf-8') as f2:
                json.dump(xxx, f2)
    except FileNotFoundError:
        with open('task_2.json', 'w', encoding='utf-8') as f2:
            f2.write('{}')
        base_()
    except KeyboardInterrupt:
        print('\n Прощай')


base_()