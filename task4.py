# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

import fractions

a, b = map(int, input('Введите первую дробь: ').split('/'))
c, d = map(int, input('Введите вторую дробь: ').split('/'))
sum_up = a*d + c*b
sum_down = b*d
pr_up = a*c
pr_down = b*d
for i in reversed(range(2, min(abs(sum_up), abs(sum_down)) + 1)):
    if sum_up % i == 0 and sum_down % i == 0:
        sum_up //= i
        sum_down //= i

for i in reversed(range(2, min(abs(pr_up), abs(pr_down)) + 1)):
     if pr_up % i == 0 and pr_down % i == 0:
        pr_up //= i
        pr_down //= i

print(f'Сумма дробей = {sum_up}/{sum_down}')
print(f'Произведение дробей = {pr_up}/{pr_down}')

f1 = fractions.Fraction(a, b)
f2 = fractions.Fraction(c, d)
print('\n А это сумма от фрактионса - ', f1 + f2)
print(' Произведение фрактионса - ', f1 * f2)
