# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# Ввод: c:/Users/Vladislav/Desktop/deep_to_python/test.txt
#
# Вывод: ( 'c:/Users/Vladislav/Desktop/deep_to_python/', 'test', '.txt')

st = 'c:/Users/Vladislav/Desktop/deep_to_python/test.txt'

def url_(st):
    *a, b = st.split('/')
    way = '/'.join(a) + '/'
    c, d = b.split('.')
    return way, c, '.' + d

print(url_(st))