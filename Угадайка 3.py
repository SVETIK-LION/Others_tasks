from random import *

num = randrange(1, 101)
count = 1
print('Добро пожаловать в числовую угадайку')
print('Введите число от 1 до 100 ʕ ᵔᴥᵔ ʔ')


# объявление функции "Защита от дурака"
def is_valid(a):
    if a.isdigit() == True and 1 <= int(a) <= 100:
        return True
    else:
        return False


# основная программа


while True:
    a = input()
    if is_valid(a) == False:
        print('А может всё-таки введете число от 1 до 100? ʕ •̀ o •́ ʔ)')
        continue

    a = int(a)

    if a < num:
        print('Ваше число меньше загаданного')
        count += 1
    elif a > num:
        print('Ваше число больше загаданного')
        count += 1
    elif a == num:
        print('Поздравляю! Вы угадали ʕ ∀ ʔﾉ*:･ﾟ✧')
        print('Количество попыток:', count)
        print('Спасибо, что сыграли со мной!')