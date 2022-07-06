import unittest
from unittest.mock import Mock, patch

# Объект тестирования
import phrase_generation
from phrase_generation import Heroes


class PhraseGenTest(unittest.TestCase):

    # def mock_generate_phrase(self, name_1: str, name_2: str, damage: int, weapon: str, type_attack: str):
    #     self.name_1 = name_1
    #     self.name_2 = name_2
    #     self.damage = damage
    #     self.weapon = weapon
    #     self.type_attack = type_attack
    #
    #     attack = [f'{name_1} сметает все на своем пути и наносит {name_2} {damage} урона своим грозным {weapon}', f'{name_1} легко подрезает {name_2} и наносит урон {damage} своим вошебным {weapon}', f'{name_2} отвлекается на обманный маневр {name_1} и получает {damage} урона тяжелым {weapon} прямо по голове']
    #     block = [f'{name_1} не так прост, поэтому блокирует нападение {name_2} и его {weapon}', f'{name_1} делает потрясающее сальто и уворачивается от {weapon} {name_2}, вот это ловкость!', f'{name_1} делает невозможное и уходит от атаки {name_2} и его {weapon}']
    #     fail = [f'Пока {name_1} готовил нападение, хитрый {name_2} уже занес свой {weapon} и дала бой, отняв {damage} здоровья', f'{name_1} никак не мог ожидать от {name_2} такой подлянки и тут же получил урон {damage} от ее сияющего волшебного {weapon}', f'Сколько бы {name_1} не уворачивался от {weapon}, {name_2} оказался быстрее и нанес {damage} урона']
    #
    #
    #     if type_attack == 'ATACK':
    #         phrase_index = randint(0, len(attack) - 1)
    #         result = attack[phrase_index]
    #         return result
    #     elif type_attack == 'BLOCK':
    #         phrase_index = randint(0, len(block) - 1)
    #         result = block[phrase_index]
    #         return result
    #     elif type_attack == 'FAIL':
    #         phrase_index = randint(0, len(fail) - 1)
    #         result = fail[phrase_index]
    #         return result
    #     else:
    #         try:
    #             raise Exception("Неверное значение атаки ¯\_(ツ)_/¯")
    #         except Exception as e:
    #             return f'{str(e)}'

    @patch('phrase_generation.Heroes')
    def test_generate_phrase(self, mock_generate_phrase):
        mock_generate_phrase.return_value = 4
        self.assertEqual(phrase_generation.Heroes.generate_phrase('Единорожка', 'Муся-Пуся', 14, 'Рог', 'ATACK', 4))
        # new_heroes = phrase_generation.Heroes()
        # new_heroes.generate_phrase = Mock(side_effect=self.mock_generate_phrase)
        # result = new_heroes.generate_phrase('Единорожка', 'Муся-Пуся', 14, 'Рог', 'ATACK')
        # self.assertEqual(phrase_generation.Heroes.generate_phrase('Единорожка', 'Муся-Пуся', 14, 'Рог', 'ATACK'),result)

    # def test_attack(self):
    #     result = generate_phrase(name_1='Единорожка', name_2='Муся-Пуся', damage=14, weapon='Рог', type_attack='ATACK')
    #     self.assertIn(result, attack)
    #
    # def test_fail(self):
    #     result = generate_phrase(name_1='Ололошка', name_2='Кентавриха', damage=6, weapon='СвинцовоеКопыто', type_attack='FAIL')
    #     self.assertIn(result, fail)
    #
    # def test_block(self):
    #     result = generate_phrase(name_1='ЧеткийГепард', name_2='БогСолнца', damage=0, weapon='ЛучиДобра', type_attack='BLOCK')
    #     self.assertIn(result, fail)
    #
    # def test_attack_value_error(self):
    #     with self.assertRaises(Exception) as e:
    #         print(generate_phrase('Кошка', 'Собака', 8, 'Когти', 'no_name'))



#
# if __name__ == "__main__":
#
