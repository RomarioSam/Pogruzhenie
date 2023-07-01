# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии
# (решение задачи "не в одну строку" есть на 4 семинаре(5 задача))

NAMES = ["Наруто", "Саске", "Сакура"]
ZP = [10000, 10000, 10000]
PREM = ['0%', '30.5%', '25%']

print({NAMES[i]: ZP[i] * float(PREM[i][:-1]) / 100 for i in range(len(NAMES))})