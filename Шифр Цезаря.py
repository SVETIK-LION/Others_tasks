#вводим данные
print('Это программа для шифровки и дешифровки текста Шифром Цезаря.')
step = int(input('Введите шаг сдвига для шифровки (шаг > 0) или дешифровки (шаг < 0)'))
text = input('Введите текст')

#строки, из которых может состоять шифр
eng = [chr(i) for i in range(65,91)] + [chr(j) for j in range(97,123)]
rus = [chr(i) for i in range(1040,1104)]

def caesar(text):
    if text[0] in eng:
        alph = eng
        power = 26
    else:
        alph = rus
        power = 32
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].isupper():
                print(alph[(alph.index(text[i]) + step) % power], end = '')
            else:
                print(alph[(alph.index(text[i]) + step) % power + power], end='')
        else:
            print(text[i], end = '')
caesar(text)