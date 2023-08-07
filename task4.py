# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину прямоугольника
# и встройте контроль недопустимых значений (отрицательных).
# Используйте декораторы свойств

# Доработаем прямоугольник и добавим экономию памяти для хранения свойств экземпляра без словаря dict.

# Изменяем класс прямоугольника. Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.

class Valid:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.name, value)


class Rect:

    __slots__ = ('_a', '_b')

    a = Valid()
    b = Valid()
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # def __setattr__(self, key, value):
    #     if value > 0:
    #         self.__dict__[key] = value

    # def get_len(self):
    #     return self.a
    #
    # # @гэт_лэн.сэтар
    # def set_len(self, value):
    #     if value > 0:
    #         self.a = value
    #
    # # @пропэрци
    # def get_hei(self):
    #     return self.b
    #
    # def set_hei(self, value):
    #     if value > 0:
    #         self.b = value
    #
    #
    # length = property(get_len, set_len)
    # heigth = property(get_hei, set_hei)
    def __str__(self):
        return f'Прямоугольник со сторонами {self.a} и {self.b}'


r = Rect(5 ,3)
print(r)
r.a = 20
r.b = 7
r.b = -15
# r.arg = 22  # error изза slots
# print(r.__dict__)
print(r)