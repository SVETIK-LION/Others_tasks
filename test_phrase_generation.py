import unittest
from unittest.mock import Mock


name_1 = 'Единорожка'
name_2 = 'Муся-Пуся'
damage = 14
weapon = 'Рог'
type_attack = 'ATACK'

attack = [f'{name_1} сметает все на своем пути и наносит {name_2} {damage} урона своим грозным {weapon}',
              f'{name_1} легко подрезает {name_2} и наносит урон {damage} своим вошебным {weapon}',
              f'{name_2} отвлекается на обманный маневр {name_1} и получает {damage} урона тяжелым {weapon} прямо по голове']

name_1 = 'ЧеткийГепард'
name_2 = 'БогСолнца'
damage = 0
weapon = 'ЛучиДобра'
type_attack = 'BLOCK'

block = [f'{name_1} не так прост, поэтому блокирует нападение {name_2} и его {weapon}',
         f'{name_1} делает потрясающее сальто и уворачивается от {weapon} {name_2}, вот это ловкость!',
         f'{name_1} делает невозможное и уходит от атаки {name_2} и его {weapon}']

name_1 = 'Ололошка'
name_2 = 'Кентавриха'
damage = 6
weapon = 'СвинцовоеКопыто'
type_attack = 'FAIL'

fail = [f'Пока {name_1} готовил нападение, хитрый {name_2} уже занес свой {weapon} и дала бой, отняв {damage} здоровья',
        f'{name_1} никак не мог ожидать от {name_2} такой подлянки и тут же получил урон {damage} от ее сияющего волшебного {weapon}',
        f'Сколько бы {name_1} не уворачивался от {weapon}, {name_2} оказался быстрее и нанес {damage} урона']

# Объект тестирования
from phrase_generation import generate_phrase

# mock = Mock(spec=attack)

class PhraseGenTest(unittest.TestCase):

    def test_attack(self):
        result = generate_phrase(name_1='Единорожка', name_2='Муся-Пуся', damage=14, weapon='Рог', type_attack='ATACK')
        self.assertIn(result, attack)

    def test_fail(self):
        result = generate_phrase(name_1='Ололошка', name_2='Кентавриха', damage=6, weapon='СвинцовоеКопыто', type_attack='FAIL')
        self.assertIn(result, fail)

    def test_block(self):
        result = generate_phrase(name_1='ЧеткийГепард', name_2='БогСолнца', damage=0, weapon='ЛучиДобра', type_attack='BLOCK')
        self.assertIn(result, fail)

    def test_attack_value_error(self):
        with self.assertRaises(Exception) as e:
            print(generate_phrase('Кошка', 'Собака', 8, 'Когти', 'no_name'))




# if __name__ == "__maine__":
#     main()

