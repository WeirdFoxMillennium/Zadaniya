import unittest

import first_ten_tasks as ftt


class TestFirstTenTasks(unittest.TestCase):

    def test_first_task(self):
        input_string = 'Привет! Как дела?'
        result = ftt.first_task(input_string)
        expected_result = '6 р. 80 коп.'
        self.assertEqual(expected_result, result)

    def test_second_task(self):
        first_string = '132'
        second_string = '144'
        third_string = '126'
        first_result, second_result, third_result = ftt.second_task(
            first_string, second_string, third_string)
        expected_first_result = '144'
        expected_second_result = '132'
        expected_third_result = '126'
        self.assertEqual(expected_first_result, first_result)
        self.assertEqual(expected_second_result, second_result)
        self.assertEqual(expected_third_result, third_result)

    def test_third_task(self):
        # Тест из задачи
        input_num = 302231454903657293676544
        result = ftt.third_task(input_num)
        expected_result = 78
        self.assertEqual(expected_result, result)

        # Проверка возвращаемоего результата, если число не является степенью 2
        input_num = 3
        result = ftt.third_task(input_num)
        expected_result = 'НЕТ'
        self.assertEqual(expected_result, result)

        # Проверка возвращаемоего результата, если число на входе 1
        input_num = 1
        result = ftt.third_task(input_num)
        expected_result = 0
        self.assertEqual(expected_result, result)

    def test_fourth_task(self):
        # Первый тестовый случай
        n = 54
        weight = 1
        height = 43
        result = ftt.fifth_task(n, weight, height)
        expected_result = 1
        self.assertEqual(expected_result, result)

        # Второй тестовый случай
        n = 46
        weight = 5
        height = 4
        result = ftt.fifth_task(n, weight, height)
        expected_result = 2
        self.assertEqual(expected_result, result)

    def test_fifth_task(self):
        pass

    def test_sixth_task(self):
        # Первый тестовый случай
        prob = 0.2
        prize = 50
        pay = 9
        result = ftt.sixth_task(prob, prize, pay)
        self.assertTrue(result)

        # Второй тестовый случай
        prob = 0.9
        prize = 1
        pay = 2
        result = ftt.sixth_task(prob, prize, pay)
        self.assertFalse(result)

        # Третий тестовый случай
        prob = 0.9
        prize = 3
        pay = 2
        result = ftt.sixth_task(prob, prize, pay)
        self.assertTrue(result)

    def test_seventh_task(self):
        pass

    def test_eighth_task(self):
        # Первый тестовый случай
        first_num = 3
        second_num = 4
        third_num = 3
        result = ftt.eighth_task(first_num, second_num, third_num)
        self.assertEqual(2, result)

        # Второй тестовый случай
        first_num = 1
        second_num = 1
        third_num = 1
        result = ftt.eighth_task(first_num, second_num, third_num)
        self.assertEqual(3, result)

        # Третий тестовый случай
        first_num = 3
        second_num = 4
        third_num = 1
        result = ftt.eighth_task(first_num, second_num, third_num)
        self.assertEqual(0, result)

    def test_ninth_task(self):
        # Первый тестовый случай
        input_data = 'Там есть бомба'
        result = ftt.ninth_task(input_data)
        self.assertEqual("ПРИГНИСЬ!", result)

        # Второй тестовый случай
        input_data = 'Эй, ты думал, там БОМБА?'
        result = ftt.ninth_task(input_data)
        self.assertEqual("ПРИГНИСЬ!", result)

        # Третий тестовый случай
        input_data = 'Это взрывается!!!'
        result = ftt.ninth_task(input_data)
        self.assertEqual("Расслабься, бомбы нет.", result)

    def test_tenth_task(self):
        # Первый тестовый случай
        input_data = 'Happy Birthday'
        result = ftt.tenth_task(input_data)
        self.assertEqual("hAPPY bIRTHDAY", result)

        # Второй тестовый случай
        input_data = 'MANY THANKS'
        result = ftt.tenth_task(input_data)
        self.assertEqual("many thanks", result)

        # Третий тестовый случай
        input_data = 'sPoNtAnEoUs'
        result = ftt.tenth_task(input_data)
        self.assertEqual("SpOnTaNeOuS", result)
