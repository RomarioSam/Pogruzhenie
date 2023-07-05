# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку

from sys import argv
from funk_sem_6 import task6

print(task6.date_inp(''.join(argv[1:])))
