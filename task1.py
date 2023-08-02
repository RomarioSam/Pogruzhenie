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

print(my.sting, my.time, my.date)
print(my.__new__.__doc__)
print(my)
print(f'{my = }')


# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

class Archive(list):
    lst = []
    def __new__(cls, num):
        instance = super().__new__(cls, num)
        instance.num = num
        instance.lst.append(num)
        return instance

f1 = Archive((10, 'sdfsdf'))
f2 = Archive((20, 'zzzzzzz'))
f3 = Archive((30, 'vvvvvvv'))
print(f1, f2, f3, f1.lst)

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



