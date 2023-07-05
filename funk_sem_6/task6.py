# Создайте модуль и напишите в нём функцию,
# которая получает на вход дату в формате DD.MM.YYYY и возвращает истину,
# если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# И весь период действует григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.


def date_inp(dat: str) -> bool:
    try:
        day, month, year = map(int, dat.split('.'))
        print('Высокосный? ', _up_year(year))
        if 0 < day < 32 and 0 < month < 13 and 0 < year < 9999:
            return True
        return False
    except:
        print('Плохо ввели')
        date_inp(input('Еще попытка: '))


def _up_year(year):
    if year % 4 == 0:
        return True
    return False

if __name__ == '__main__':
    print("Ввели верно?", date_inp(input('Даувай: ')))
