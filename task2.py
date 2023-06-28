# Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
#
# целое положительное число
# вещественное положительное или отрицательное число
# строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# строку в верхнем регистре в остальных случаях

inp = input('Ввод: ')
if inp.isdigit():
    print(int(inp))
elif inp[0] == '-' and inp[1:].isdigit():
    print(float(inp))
elif inp.count('.') == 1:
    a1, a2 = inp.split('.')
    if (a1.isdigit() and a2.isdigit()) or (a1[0] == '-' and a1[1:].isdigit() and a2.isdigit()):
        print(float(inp))
elif inp != inp.lower():
    print(inp.lower())
else:
    print(inp.upper())
