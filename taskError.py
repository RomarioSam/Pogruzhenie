class Error112(Exception):

    def __init__(self, a, b):
        self.x = a if isinstance(a, str) else b

    def __str__(self):
        return f'Прямоугольник не может быть со сторонами строковых значений. {self.x} - строка, а не число'

class Error212(Exception):
    def __init__(self, a, b):
        self.x = a if a <= 0 else b

    def __str__(self):
        return f'Прямоугольник не может быть со стороной {self.x}'


