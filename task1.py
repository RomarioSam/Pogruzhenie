# class Person:
#     max_up = 3
#     def __init__(self, name, race='unknown'):
#         self.level = 2
#         self.health = 300
#         self.name = name
#         self.race = race
#         print(id(self), 'dsdsd')
#
#
# p1 = Person('Roma', 'Elph')
# p2 = Person('Petya')
# print(id(p1))
# print(id(p2))
# print(p1.name, p1.race, p2.name, p2.race)


# class Circle():
#     def __init__(self, r):
#         self.length = 2 * 3.14 * r
#         self.square = r * r * 3.14
#
#
# cir1 = Circle(5)
# cir2 = Circle(18)
# print(cir1.length, cir1.square, cir2.length, cir2.square)


# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат

# class Rectangle():
#     def __init__(self, a, b=None):
#         if b == None: b = a
#         self.perimeter = 2 * (a + b)
#         self.square = a * b
#
# rect1 = Rectangle(6 , 7)
# rect2 = Rectangle(4)
#
# print(rect1.perimeter, rect1.square, rect2.perimeter, rect2.square)

# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.


class Person():
    def __init__(self, fio, age):
        self.fio = fio
        self._age = age

    def birthday(self):
        self._age += 1

    def full_name(self):
        print(self.fio)


# p1 = Person('Sasha', 25)
# p2 = Person(input('введите фио'), int(input('ваш возраст')))
# p1.birthday()
# print(p1._age)
# p1.full_name()


# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

class Sotrudnik(Person):
    def __init__(self, idd, *args):
        super().__init__(*args)
        self.idd = idd
        self.dostup = idd % 7


# p2 = Sotrudnik(343638, 'sfddfd', 18)
# p2.fio = 'Lesha Ivanov'
# p3 = Sotrudnik(23423, 'fdsfs', 23)
#
# print(p2.dostup, p2.fio, p2._age)
# print(p3.fio, p3.dostup, p3._age)

# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.


class Animal():
    def __init__(self, name, age, length, mass, color, oreal):
        self.name = name
        self.age = age
        self.length = length
        self.mass = mass
        self.color = color
        self.oreal = oreal

class Fish(Animal):
    def __init__(self, plavn, zubi, *args, **kwargs):
        self.plavn = plavn
        self.zubi = zubi
        super().__init__(*args, **kwargs)
    def printing(self):
        print(self.plavn, self.zubi)

class Bird(Animal):
    def __init__(self, cluf, visota, *args, **kwargs):
        self.cluf = cluf
        self.visota = visota
        super().__init__(*args, **kwargs)
    def printing(self):
        print(self.cluf, self.visota)

class Kopitnii(Animal):
    def __init__(self, siedobnost, *args, **kwargs):
        self.siedobnost = siedobnost
        super().__init__(*args, **kwargs)
    def printing(self):
        print(self.siedobnost)

anim1 = Fish(plavn='красные', zubi='маленькие', name='красноперка', age='3 года',
             color='серый', length='25sm', mass='200gr', oreal='озера, реки')

anim1.printing()


# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.
# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.

