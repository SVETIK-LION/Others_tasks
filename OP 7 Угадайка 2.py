#Игра "Угадайка"
from random import *
print('Ку-ку, я Ваш компьютер :) Загадайте число от 1 до 100, а я буду угадывать')
min_num = 1
max_num = 100
result = None
while result != '=':
    number = randint(min_num, max_num)
    print(f'Это число {number}?')
    result = input('Если я угадал, то введите "=". Если загаданное число больше моего, то ">". А если меньше, то "<": ')
    if result == '>':
        min_num = number + 1
    elif result == '<':
        max_num = number - 1
print('Ура! Я угадал ^_^')