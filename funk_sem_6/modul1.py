from random import randint as rin


def funk1(arg1=10, arg2=100, k=5):
    x = rin(arg1, arg2 + 1)
    print(f'\n Компуктер загадал целое число от {arg1} до {arg2}. Отгадывайте, у вас {k} попыток.\n')
    n = 1
    # print(x)
    while k > 0:
        inp = int(input(f'{n} попытка: '))
        if inp == x:
            print('Истина!')
            return
        elif inp < x and k > 1:
            print("Надo больше")
        elif inp > x and k > 1:
            print('Надо меньше')
        n += 1
        k -= 1
    print('Ложь!')

COUNT_POPITOK = {}

def zagad_(zagad, otv, count=3):
    print(f'\n {zagad}: \n')
    while count > 0:
        inp = input('Vvedite otvet: ').lower()
        if inp in otv:
            print(count)
            count_zagad(zagad, count)
            return
        count -= 1
    count_zagad(zagad, count)
    print(count)


def spisok_zagadok():
    SPISOK = {'Зимой и летом одним цветом': ["сосна", "ель"],
              'Заплелись густые травы, Закудрявились луга, Да и сам я весь кудрявый, Даже завитком рога.': ['баран'],
              'У него огромный рот, Он зовется …': ['бегемот'],
              }
    for k, v in SPISOK.items():
        zagad_(k, v)


def count_zagad(zag, count):
    COUNT_POPITOK[zag] = count

