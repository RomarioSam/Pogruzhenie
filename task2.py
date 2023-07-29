# Дорабатываем задачу 1. Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию-угадайку числа
# в диапазоны [1, 100] и [1, 10]. Если не входят,
# вызывать функцию со случайными числами из диапазонов.


from random import randint as rnd

MIN_NUMB = 1
MAX_NUMB = 100
MIN_COUNT = 1
MAX_COUNT = 10
def game(func):
    def wrapper(num, count):
        if num < MIN_NUMB or num > MAX_NUMB:
            num = rnd(MIN_NUMB, MAX_NUMB)
        if count < MIN_COUNT or count > MAX_COUNT:
            count = rnd(MIN_COUNT, MAX_COUNT)
        func(num, count)
    return wrapper


@game
def inp(num, count):
    for _ in range(count):
        user_number = int(input('Введите число: '))
        if user_number == num:
            print('Угадали')
            return True
        elif user_number < num:
            print('Число больше')
        else:
            print('Число меньше')
    print('Попытки кончились')


inp(50, 11)

