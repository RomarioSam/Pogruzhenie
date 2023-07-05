from random import randint as rd


def chess_position():  # заполняем рандомом расположение 8ми ферзей. заполняем так, что они не стоят на одних
    sp1 = [1, 2, 3, 4, 5, 6, 7, 8]  # линиях по вертикали или горизонтали
    sp_position = []
    for i in range(1, 9):
        rand = rd(0, len(sp1) - 1)
        sp_position.append([i, sp1[rand]])
        sp1.pop(rand)
    return sp_position


def step_queen(ferz):  # заполняем массив возможными ходами по диагонали очередной ферзи
    steps = []
    alt, long = ferz
    while alt < 8 and long < 8:
        alt += 1
        long += 1
        steps.append([alt, long])
    alt, long = ferz
    while alt < 8 and long > 1:
        alt += 1
        long -= 1
        steps.append([alt, long])
    alt, long = ferz
    while alt > 1 and long > 1:
        alt -= 1
        long -= 1
        steps.append([alt, long])
    alt, long = ferz
    while alt > 1 and long < 8:
        alt -= 1
        long += 1
        steps.append([alt, long])
    return steps


def atacking_chess(matr):  # проверяем, стоит ли другая ферзя на возможных ходах очередной ферзи
    for ferz in matr:
        for other_ferz in matr:
            if other_ferz in step_queen(ferz):
                return False
    return True


def counts_positions(COUNT_POSITION):
    count = 0
    while count < COUNT_POSITION:
        pos = chess_position()
        if atacking_chess(pos):
            count += 1
            paint_positions(pos)
            print()

def paint_positions(pos):
    pusto = '□'
    ferzik = '■'
    for i in pos:
        for j in range(8):
            if j + 1 == i[1]:
                print('■', end='  ')
            else:
                print('□', end='  ')
        print()


