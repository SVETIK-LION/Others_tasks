from random import *
numbers = []

def compare_ans(user_answer, answer):
    if user_answer == answer:
        print('Правильно!')
    else:
        print('Неверный ответ :( Правильное число', answer)

#Хочу написать функцию для генерации случайной позиции числа, которое должен угадать пользователь. Но как эту функцию поместить user_answer?
# def random_number(n):
#     position = randrange(n)
#     return position

print('Это программа-тренажер для тренировки памяти')

n = int(input('Введите количество чисел, которые Вы готовы замомнить: '))

for _ in range(n):
    num = randrange(1, 100)
    numbers.append(num)

random_number(n)

print('Запомните эти числа')
print(*numbers)
print('Не подглядывать! ;)')

user_answer = int(input('Каким было первое число?: '))
compare_ans(user_answer, numbers[0])

user_answer = int(input('Каким было последнее число?: '))
compare_ans(user_answer, numbers[-1])

user_answer = int(input('Каким было четвертое число?: '))
compare_ans(user_answer, numbers[3])