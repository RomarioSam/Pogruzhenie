from taskError import Error112, Error212


# прямоугольник

class Rect:

    def __init__(self, a, b):
        if isinstance(a, str) or isinstance(b, str):
            raise Error112(a, b)
        elif a <= 0 or b <= 0:
            raise Error212(a, b)
        self.a = a
        self.b = b

    def __str__(self):
        return f' Прямоугольник со стронами {self.a} и {self.b} '


r1 = Rect(3, '4')
r2 = Rect(3, -4)
r3 = Rect(5, 7)
