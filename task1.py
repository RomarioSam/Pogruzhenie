# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)

import time


class My_string(str):
    '''Создание через new, через создание экземпляра строки'''

    def __new__(cls, sting, date):
        '''Cozdanie new'''
        ins = super().__new__(cls, sting)
        ins.sting = sting
        ins.date = date
        ins.time = time.time()
        return ins

    def __str__(self):
        return f'Представление для пользователя {self.sting} {self.time:0.2f}'

    def __repr__(self):
        return f'Представление для программиста {self.sting} {self.time:0.2f}'


my = My_string('Roman S', 1123)


# print(my.sting, my.time, my.date)
# print(my.__new__.__doc__)
# print(my)
# print(f'{my = }')


# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

class Archive(list):
    '''sdf  s  sdfsdldkavkdhg ahgdkahdg gaskaysbdayd'''
    lst = []

    def __new__(cls, num):
        instance = super().__new__(cls, num)
        instance.num = num
        instance.lst.append(num)
        return instance

    def __str__(self):
        return f'Значения {instance.num[0]} {instance.num[1]}'


# f1 = Archive((10, 'sdfsdf'))
# f2 = Archive((20, 'zzzzzzz'))
# f3 = Archive((30, 'vvvvvvv'))
# print(f1, f2, f3, f1.lst)

# Добавьте к задачам 1 и 2 строки документации для классов.
# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.

# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.


class Rectangle():
    '''sdfds ffdfsd sdfdsf.hfdshfb hkhga kzhdgka '''

    def __init__(self, a, b=None):
        if b == None: b = a
        self.a = a
        self.b = b
        self.perimeter = 2 * (a + b)
        self.square = a * b

    def __add__(self, other):
        p = self.perimeter + other.perimeter
        a = self.a + other.a
        b = int(p / 2 - a)
        return Rectangle(a, b)

    def __sub__(self, other):
        p = abs(self.perimeter - other.perimeter)
        a = abs(self.a - other.a)
        b = int(p / 2 - a)
        return Rectangle(a, b)

    def __eq__(self, other):
        return self.square == other.square

    def __lt__(self, other):
        return self.square < other.square

    def __le__(self, other):
        return self.square <= other.square

    def __str__(self):
        return f'Прямоугольник со сторонами {self.a} и {self.b}'


rect1 = Rectangle(6, 7)
rect2 = Rectangle(4)
rect3 = rect1 + rect2
print(f'3 rect... a = {rect3.a}, b = {rect3.b}, perimeter = {rect3.perimeter}')
rect4 = rect1 - rect2
print(f'4 rect... a = {rect4.a}, b = {rect4.b}, perimeter = {rect4.perimeter}')

# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

print(rect1 == rect3)

# Добавьте ко всем задачам с семинара строки документации и методы вывода
# информации на печать.
# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц

print(rect3)


class Matrix():

    def __init__(self, matr):
        self.matr = matr

    def __eq__(self, other):
        return len(self.matr[0]) * len(self.matr) == len(other.matr[0]) * len(other.matr)

    def __gt__(self, other):
        return len(self.matr[0]) * len(self.matr) > len(other.matr[0]) * len(other.matr)

    def __ge__(self, other):
        return len(self.matr[0]) * len(self.matr) >= len(other.matr[0]) * len(other.matr)

    def __add__(self, other):
        if len(self.matr[0]) > len(other.matr[0]):
            x = len(self.matr[0]) - len(other.matr[0])
            for i in range(len(other.matr)):
                for _ in range(x):
                    other.matr[i].append(0)
        if len(self.matr[0]) < len(other.matr[0]):
            x = len(other.matr[0]) - len(self.matr[0])
            for i in range(len(self.matr)):
                for _ in range(x):
                    self.matr[i].append(0)
        if len(self.matr) > len(other.matr):
            x = len(self.matr) - len(other.matr)
            for _ in range(x):
                other.matr.append([0 for i in range(len(self.matr[0]))])
        if len(self.matr) < len(other.matr):
            x = len(other.matr) - len(self.matr)
            for _ in range(x):
                self.matr.append([0 for i in range(len(other.matr[0]))])
        m3 = [[self.matr[i][j] + other.matr[i][j] for j in range(len(self.matr[0]))] for i in range(len(self.matr))]
        return Matrix(m3)

    def __mul__(self, other):
        '''прописывать код для создания подходящего размера матриц не буду :('''
        m3 = []
        for i in range(len(self.matr)):
            lst = []
            for j in range(len(self.matr)):
                sum = 0
                for k in range(len(self.matr[0])):
                    sum += self.matr[i][k] * other.matr[k][j]
                lst.append(sum)
            m3.append(lst)
        return Matrix(m3)

    def __str__(self):
        return f'Матрица {len(self.matr[0])} на {len(self.matr)}'


m1 = Matrix([[1, 2, 3], [7, 8, 7], [9, 6, 4], [7, 8, 4]])
m2 = Matrix([[7, 3], [6, 2], [9, 8]])
m3 = Matrix([[4, 8, 5], [2, 3, 7]])
m4 = Matrix([[2, 3], [6, 7], [9, 1]])
print(m2 >= m1)

m0 = m2 + m1
print(f'сумма матриц м1 и м2 = {m0.matr}')

print(f'1 матрица для перемножения {m3.matr}')
print(f'2 матрица для перемножения {m4.matr}')
m5 = m3 * m4
m6 = m4 * m3
print(f'Результат перемножения 1ой на 2ую = {m5.matr}')
print(f'Результат перемножения 2ой на 1ую ={m6.matr}')