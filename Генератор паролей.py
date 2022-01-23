from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
iskl = 'il1Lo0O'
chars = ''

print('Сколько паролей Вы хотите сгенерировать?')
kolvo_par = int(input())

print('Какая должна быть длина пароля? ')
lenght = int(input())

print('Включить ли прописные буквы? ABCDEFGHIJKLMNOPQRSTUVWXYZ да/нет ')
propis = input()

print('Включить ли строчные буквы? abcdefghijklmnopqrstuvwxyz да/нет ')
stroch = input()

print('Включить ли символы? !#$%&*+-=?@^_ да/нет ')
sym = input()

print('Исключить ли неоднозначные символы? il1Lo0O да/нет ')
neodn = input()

if propis.lower() == 'да':
    chars += uppercase_letters
else:
    chars = chars

if stroch.lower() == 'да':
    chars += lowercase_letters
else:
    chars = chars

if sym.lower() == 'да':
    chars += punctuation
else:
    chars = chars

if iskl.lower() == 'нет':
    chars += neodn
else:
    chars = chars

if lenght > len(chars):
    print('Недостаточно символов')


def generate_password(lenght, chars):
    password = ''
    for i in range(int(lenght)):
        password += choice(chars)
    print(password)


for j in range(1, (kolvo_par) + 1):
    generate_password(lenght, chars)