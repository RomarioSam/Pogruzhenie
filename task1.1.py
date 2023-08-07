# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений. Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых чисел и их факториалов.
# Доработаем задачу 1. Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
import json
class Facktor():


    def __init__(self, k):
        self.sp = []
        self.k = k

    def __call__(self, n, *args, **kwargs):
        pr = 1
        for i in range(1, n + 1):
            pr *= i
        self.sp.append({n: pr})
        if len(self.sp) > self.k:
            self.sp.pop(0)
        return self.sp[-1]

    def memory(self):
        return print(self.sp)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('memory_fack.json', 'w') as f1:
            json.dump(self.sp, f1)


f = Facktor(3)
print(f(5))
print(f(7))
print(f(8))
print(f(10))
# print(f(12))
f.memory()
with f:
    pass

            




