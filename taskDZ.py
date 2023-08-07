# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

import csv
from random import randint as rnd

MIN_GRADE = 2
MAX_GRADE = 5
MIN_BALL = 0
MAX_BALL = 100
lessons = ['русский язык', 'физкультура', "английский язык", "история", "физика", \
           "химия", "информатика", "математика", "биология", "изо", "труды"]
class Val_Fio:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        letters = ' -qwertyuiopasdfghjklzxcvbnmёйцукенгшщзхъфывапролджэячсмитьбю'
        letters += letters.upper()
        xxx = 0
        for i in value:
            if i in letters:
                xxx += 1
        if len(value) == xxx:
            val_fio = value.split()
            if len(val_fio) == 3:
                for i in val_fio:
                    if i.istitle():
                        xxx += 1
                if xxx == len(value) + 3:
                    setattr(instance, self.name, value)


class Stud():

    fio = Val_Fio()
    def __init__(self, fio):
        self.fio = fio
        family = self.fio.split()[0]
        with open(f'predmetes{family}.csv', 'w', newline='', encoding='utf-8') as f:
            wr = csv.writer(f, quotechar='_', delimiter='|', quoting=csv.QUOTE_MINIMAL)  # создали csv
            xxx = ([[i, [rnd(MIN_GRADE, MAX_GRADE) for _ in range(5)],                   # магические числа
                      [rnd(MIN_BALL, MAX_BALL) for _ in range(3)]] for i in lessons])
            for i in xxx:
                wr.writerow(i)
        with open(f'predmetes{family}.csv', 'r', encoding='utf-8') as f:
            predm = []
            test = {}
            grade_sum = 0
            rr = csv.reader(f, dialect='excel-tab')
            for i in rr:
                for j in i:
                    xxx = j.split('|')
                    predm.append(xxx[0])
                    test_grades = int(sum([int(i) for i in xxx[2][1:-1].split(', ')]) / 3)
                    test[xxx[0]] = test_grades             # магические числа
                    grade_sum += int(sum([int(i) for i in xxx[1][1:-1].split(', ')]))
        self.test = test
        self.grade = grade_sum / (len(predm) * 5)
        self.__predm = predm
    @property
    def predm(self):
        return self.__predm.copy()
    @predm.setter
    def predm(self, value):
        raise ValueError('Нельзя менять')


pip1 = Stud('Афанасьев Валерий Vалерьевич')
print(pip1.fio)
print(pip1.predm)
pip1.predm.append('sdfdds')
print(pip1.predm)
print(pip1.test)
print(pip1.grade)



