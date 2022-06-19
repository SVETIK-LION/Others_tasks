from random import randint


def generate_phrase(name_1: str, name_2: str, damage: int, weapon: str, type_attack: str):
    attack = [f'{name_1} сметает все на своем пути и наносит {name_2} {damage} урона своим грозным {weapon}', f'{name_1} легко подрезает {name_2} и наносит урон {damage} своим вошебным {weapon}', f'{name_2} отвлекается на обманный маневр {name_1} и получает {damage} урона тяжелым {weapon} прямо по голове']
    block = [f'{name_1} не так прост, поэтому блокирует нападение {name_2} и его {weapon}', f'{name_1} делает потрясающее сальто и уворачивается от {weapon} {name_2}, вот это ловкость!', f'{name_1} делает невозможное и уходит от атаки {name_2} и его {weapon}']
    fail = [f'Пока {name_1} готовил нападение, хитрый {name_2} уже занес свой {weapon} и дала бой, отняв {damage} здоровья', f'{name_1} никак не мог ожидать от {name_2} такой подлянки и тут же получил урон {damage} от ее сияющего волшебного {weapon}', f'Сколько бы {name_1} не уворачивался от {weapon}, {name_2} оказался быстрее и нанес {damage} урона']

    if type_attack == 'ATACK':
        phrase_index = randint(0, len(attack) - 1)
        result = attack[phrase_index]
        return result
    elif type_attack == 'BLOCK':
        phrase_index = randint(0, len(block) - 1)
        result = block[phrase_index]
        return result
    elif type_attack == 'FAIL':
        phrase_index = randint(0, len(fail) - 1)
        result = fail[phrase_index]
        return result
    else:
        try:
            raise Exception("Неверное значение атаки ¯\_(ツ)_/¯")
        except Exception as e:
            return f'{str(e)}'



print(generate_phrase('Единорожка', 'Муся-Пуся', 14, 'Рог', 'ATACK'))
print(generate_phrase('Ололошка', 'Кентавриха', 6, 'СвинцовоеКопыто', 'FAIL'))
print(generate_phrase('ЧеткийГепард', 'БогСолнца', 10, 'ЛучиДобра', 'BLOCK'))
print(generate_phrase('Кошка', 'Собака', 8, 'Когти', 'no_name'))

