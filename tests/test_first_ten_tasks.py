import unittest

import first_ten_tasks as ftt


class TestFirstTenTasks(unittest.TestCase):

    def test_first_task(self):
        input_string = 'Привет! Как дела?'
        result = ftt.first_task(input_string)
        expected_result = '6 р. 80 коп.'
        self.assertEqual(expected_result, result)


