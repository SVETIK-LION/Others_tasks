print('Программа для рассчета вклада')
count = 1
deposit = int(input('Введите сумму вклада: '))
percent = int(input('Введите процент: '))

for i in range(5):
    sum_percent = deposit * (percent/100)
    deposit = deposit + sum_percent
    print(f'{count} год: {deposit}')
    print(f'Сумма процентов: {sum_percent}')
    count += 1