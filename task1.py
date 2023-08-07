from collections import defaultdict

class Numbur():

    def __init__(self):
        self.stor = defaultdict(list)

    def __str__(self):
        return f'алала... {self.stor}'

    def __call__(self, v):
        self.stor[type(v)].append(v)
        return f'добавили ключ {type(v)} значение {v}'



# n = Numbur()
# print(n(42))
# print(n('333333'))
# print(n(23))
# print(n(42))
# print(n('42'))
# print(n)

class Ituretor():

    def __init__(self, start, stop):
        self.start = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.stop - 1:
            self.start += 1
            return self.start
        raise StopIteration

    def __set_name__(self, owner, name):
        print('проходим SETNAME')
        self.name = 'zz' + name
        print(f'{self.start}  {owner}  {name}  {self.name}')

    def __get__(self, instance, owner):
        print('проходим GET')
        print(f'{self.name}  _____________  {instance}  __________  {owner}')
        return Ituretor(self.start, self.stop)

    def __set__(self, instance, value):
        print('проходим SET')
        print(f'{self.__dict__}  ----   {instance.__dict__}   -----   {value}')
        self.start = value[0]
        self.stop = value[1]

# x = Ituretor(-22, -20)
# for i in x:
#     print(i)

# class Itera():
#     iii = Ituretor(20, 24)
#     xxx = Ituretor(0, 5)
#
#     def __init__(self):
#         self.rrr = self.xxx
#         # self.name = 'tratata'
#         # self.iii = (144, 150)
#         # self.xxx = 'pukpukupkuu'
#         print()
#
# uuu = Itera()
# for i in uuu.rrr:
#     print(i)
#
#
# uuu.iii = (66, 70)
# for i in uuu.iii:
#     print(i)


class x111():
    def __init__(self, p):
        self.p = p
        print(2)

    def __set_name__(self, owner, name):
        self.param_name = '_' + name
        print(3)

    def __set__(self, instance, value):
        print(instance.__dict__, value)
        if self.p(value):
            print(6)
            setattr(instance, self.param_name, f'{value}value')
        else:
            raise ValueError(f'Bad {value}')

class User():
    print(1)
    fff = x111(str.istitle)

    def __init__(self, f_name, l_name):
        print(5)
        self.fff = f_name
        print(7)
        self.l_name = l_name

print(4)
# stud = User('Vан', "Гог")
# print(stud.__dict__)


