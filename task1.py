# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.

def sp(a: str) -> list:
    l = sorted(list(map(lambda x: ord(x), a)), reverse=True)
    return print(l)

sp(input('Ввод: '))