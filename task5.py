# Создайте вручную список с повторяющимися целыми числами.
# Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# Нумерация начинается с единицы.

sp = [ 3, 3, 5,4, 2, 2, 6 , 5]
sp2 = []
for i, j in enumerate(sp):
    if j % 2 != 0:
        sp2.append(i + 1)
print(sp2)