import pytest

from taskError import Error112, Error212


# прямоугольник

class Rect:
    """
    >>> r1 = Rect(3, 7)
    >>> r2 = Rect(2, '4')
    Traceback (most recent call last):
        ...
    taskError.Error112: Прямоугольник не может быть со сторонами строковых значений
    >>> r3 = Rect(-1, 3)
    Traceback (most recent call last):
        ...
    taskError.Error212: Прямоугольник не может быть со стороной меньше нуля
    """
    def __init__(self, a, b):
        if isinstance(a, str) or isinstance(b, str):
            raise Error112(a, b)
        elif a <= 0 or b <= 0:
            raise Error212(a, b)
        self.a = a
        self.b = b

    def __str__(self):
        return f' Прямоугольник со стронами {self.a} и {self.b} '



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

    import unittest
    class TestUni(unittest.TestCase):
        def test_method1(self):
            with self.assertRaises(Error212):
                r4 = Rect(-1, 3)

        def test_method2(self):
            with self.assertRaises(Error112):
                r5 = Rect(4, '3')
    unittest.main(verbosity=2)


# чтобы пайтест работал, нужно закоментить предыдущие тесты
import pytest
def test_rect1():
    with pytest.raises(Error212, match=r''):
        r6 = Rect(-1, 3)
def test_rect2():
    with pytest.raises(Error112, match=r''):
        r7 = Rect('3', 2)
pytest.main(['-v'])