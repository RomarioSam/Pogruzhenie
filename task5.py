# Объедините функции из прошлых задач. Функцию угадайку задекорируйте декораторами для сохранения параметров,
# декоратором контроля значений и декоратором для многократного запуска. Выберите верный порядок декораторов.

from random import randint as rnd
import json
from functools import wraps

MIN_NUMB = 1
MAX_NUMB = 100
MIN_COUNT = 1
MAX_COUNT = 10
N = 1 # Количество попыток
def game(func):
    @wraps(func)
    def wrapper(num, count):
        if num < MIN_NUMB or num > MAX_NUMB:
            num = rnd(MIN_NUMB, MAX_NUMB)
        if count < MIN_COUNT or count > MAX_COUNT:
            count = rnd(MIN_COUNT, MAX_COUNT)
        func(num, count)
    return wrapper


def decor(func):

    with open(f"{func.__name__}.json", 'r', encoding='utf-8') as log:
        data = json.load(log)

    @wraps(func)
    def wrapper(*args, **kwargs):
        temp_dict = func(*args, **kwargs)
        data.append(temp_dict)
        with open(f"{func.__name__}.json", 'w', encoding='utf-8') as log:
            json.dump(data, log, indent=4, ensure_ascii=False)

    return wrapper

def counter(n):
    lst_counter = []

    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                lst_counter.append(func(*args, **kwargs))
            return lst_counter
        return wrapper
    return deco


@counter(N)
@game
@decor
def inp(num, count):
    """Угадайка"""
    x = 1
    for _ in range(count):
        user_number = int(input('Введите число: '))
        if user_number == num:
            print('Угадали')
            return {f'Число {num}': f'Отгадали с {x} попытки'}
        elif user_number < num:
            print('Число больше')
        else:
            print('Число меньше')
        x += 1
    print('Попытки кончились')
    return {f'Число {num}': f'не отгадали за {count} попыток'}


inp(-34, 3)
print(inp.__name__)
help(inp)