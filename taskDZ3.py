import json

NALOG_SUM = 5_000_000  # баланс, при котором будет вычитан налог
PROC_NALOG = 0.9  # процент налога при балансе свыше NALOG_SUM
N = 0  # начальное количество операций
N_PROC = 3  # нужное количество операций для процентов
PROC_UP = 1.03  # начисление процентов после количества операций
MIN_COMIS = 30  # Процент за снятие минимальный
MAX_COMIS = 600  # Процент за снятие максимальный
PROC_COMIS = 0.015  # Процент за снятие
MULT = 50  # кратность пополнения и снятия


def start_(balance, n, name_):
    if n % N_PROC == 0 and n != 0:
        print(' После каждой третей операции пополнения или снятия начисляются проценты - 3%\n')
        balance *= PROC_UP
    go = input(f' Баланс = {balance}\n пополнить - 1,\n снять - 2,\n выйти - 0\n Ваше действие: ')
    if go == '0':
        print('\n  До свидания! ')
        with open('cards.txt', 'r+', encoding='utf-8') as data:
            x = data.read()
            if x == '':
                x = dict()
            else:
                x = eval(x)
            x[name_] = [balance, n]
        with open('cards.txt', 'w', encoding='utf-8') as data:
            data.write(str(x))
        return
    elif go == '1':
        top_up(balance, n, name_)
    elif go == '2':
        withdraw(balance, n, name_)
    else:
        print('Неправильна введена команда. Повторите попытку\n')
        start_(balance, n, name_)


def withdraw(balance, n, name_):
    try:
        balance = nalog(balance)
        if balance < MIN_COMIS + MULT:
            print('\n У вас недостаточно средств для минимального снятия')
            start_(balance, n, name_)
            return
        print('\n Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.')
        wi = int(input(f' Баланс = {balance}\n  Сумма снятия должна быть кратна 50 у.е.\n Введите сумму: '))
        if wi * PROC_COMIS < MIN_COMIS and wi > balance - MIN_COMIS:
            print('\n Нельзя снять больше, чем на счёте с учетом комиссии')
            withdraw(balance, n, name_)
        elif wi * PROC_COMIS < MAX_COMIS and wi > balance - wi * PROC_COMIS:
            print('\n Нельзя снять больше, чем на счёте c учетом комиссии')
            withdraw(balance, n, name_)
        elif wi * PROC_COMIS >= MAX_COMIS and wi > balance - MAX_COMIS:
            print('\n Нельзя снять больше, чем на счёте c учетом комиссии')
            withdraw(balance, n, name_)
        elif wi % MULT != 0:
            print('\n Сумма не кратна 50')
            withdraw(balance, n, name_)
        else:
            print('\n Операция успешно завершена\n')
            n += 1
            if wi * PROC_COMIS < MIN_COMIS:
                start_(balance - wi - MIN_COMIS, n, name_)
            elif wi * PROC_COMIS < MAX_COMIS:
                start_(balance - wi - wi * PROC_COMIS, n, name_)
            else:
                start_(balance - wi - MAX_COMIS, n, name_)
    except:
        print('Неправильно введена сумма снятия')
        withdraw(balance, n, name_)


def top_up(balance, n, name_):
    try:
        balance = nalog(balance)
        top = int(input(f' Баланс = {balance}\n Сумма пополнения должна быть кратна 50 у.е.\n Введите сумму: '))
        if top % MULT != 0:
            print('Сумма не кратна 50\n')
            top_up(balance, n, name_)
        else:
            if balance + top >= NALOG_SUM:
                print(f'При балансе свыше в {NALOG_SUM} , будет вычитываться налог на богатство 10% '
                      'перед каждой операцией, даже ошибочной!')
            print('\n Операция успешно завершена \n')
            n += 1
            start_(balance + top, n, name_)

    except:
        print('Неправильно введена сумма пополнения\n')
        top_up(balance, n, name_)


def nalog(balance):
    if balance > NALOG_SUM:
        print(f'\n Внимание. Ваш баланс свыше {NALOG_SUM} у.е. вычитывается налог на богатство 10% '
              'перед каждой операцией, даже ошибочной! ')
        return balance * PROC_NALOG
    else:
        return balance


def person():
                 # буду благодарен за подсказку, как сделать правильней создание файла
                 # так как  можно получить ошибку, если файла нет еще
    try:
        with open('cards.txt', 'r', encoding='utf-8') as data:
            x = data.read()
            if x == '':
                x = dict()
            else:
                x = eval(x)
        name_ = input('Введите имя владельца карты: ')
        balance, n = x.setdefault(name_, [0, 0])
        return start_(balance, n, name_)
    except:
        with open('cards.txt', 'a', encoding='utf-8') as data:
            person()


person()
