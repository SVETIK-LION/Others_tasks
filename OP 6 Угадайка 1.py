#Игра угадай число
#Загадываем случайное число
from random import *
num = randint(1, 100)
num_user = None
count = 0
levels = {1: 10, 2: 5, 3: 3}

#Просим выбрать уровень сложности
level = int(input('Выберете уровень сложности (1, 2, 3): '))
max_count = levels[level]

#Выбор количества пользователей
user_count = int(input('Введите количество пользователей: '))
users = []
for i in range(user_count):
    user_name = input(f'Введите имя пользователя № {i+1}: ')
    users.append(user_name)

is_winner = False
winner_name = None

while not is_winner:
    count += 1
    if count > max_count:
        print('Все пользователи проиграли')
        break
    print(f'Попытка № {count}')
    for user in users:
        print(f'Ход пользователя {user}')
        # Просим пользователя ввести число
        num_user = int(input('Введите число от 1 до 100: '))
        if num_user == num:
            is_winner = True
            winner_name = user
            break
        #Сравним числа
        elif num < num_user:
            print('Ваше число больше загаданного')
        else:
            print('Ваше число меньше загаданного')
else:
    print(f'Поздравляю, {winner_name}! Вы угадали <3')