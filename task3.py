# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1. Если передан один параметр, также считаем start=1.

class Giniratar():

    def __init__(self, start, stop=None, step=1):
        self.start = start
        self.stop = stop
        if stop == None:
            self.stop = start
            self.start = 1
        self.step = step
        self.f = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.stop:
            raise StopIteration
        self.f *= self.start
        self.start += self.step
        return self.start - self.step, self.f


gg = Giniratar(1, 9, 3)
for i in gg:
    print(i)
