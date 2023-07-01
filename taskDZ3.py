# Создайте функцию генератор чисел Фибоначчи

N = 10


def fib():
    num = [1, 1]
    for _ in range(1000):
        num.append(num[len(num) - 1] + num[len(num) - 2])
        yield num[len(num) - 1]


x = iter(fib())
for _ in range(N):
    print(next(x))
