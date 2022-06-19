import unittest


# Объект тестирования
from phrase_generation import generate_phrase


class PhraseGenTest(unittest.TestCase):

    def test_attack(self):
        result = generate_phrase('Единорожка', 'Муся-Пуся', 14, 'Рог', 'ATACK')
        self.assertEqual('Единорожка легко подрезает Муся-Пуся и наносит урон 14 своим вошебным Рог', 'Муся-Пуся отвлекается на обманный маневр Единорожка и получает 14 урона тяжелым Рог прямо по голове', 'Единорожка сметает все на своем пути и наносит Муся-Пуся 14 урона своим грозным Рог', result)

    # def test_fail(self):
    #     result = generate_phrase('Ололошка', 'Кентавриха', 6, 'СвинцовоеКопыто', 'FAIL')
    #     self.assertEqual('Ололошка никак не мог ожидать от Кентавриха такой подлянки и тут же получил урон 6 от ее сияющего волшебного СвинцовоеКопыто', result)
    #
    # def test_block(self):
    #     result = generate_phrase('ЧеткийГепард', 'БогСолнца', 0, 'ЛучиДобра', 'BLOCK')
    #     self.assertEqual('ЧеткийГепард делает потрясающее сальто и уворачивается от ЛучиДобра БогСолнца, вот это ловкость!', result)
    #
    # def mistake_test(self):

