import unittest
from main import check_time, get_time


class TestTimeRegex(unittest.TestCase):

    def test_valid_times(self):
        """Проверка корректных значений времени"""
        valid_times = ["00:00:00", "12:30:45", "23:59:59", "09:05:07", "00:00:14",
                       "00:11:22", "12:34:56", "11:11:11", "23:23:23", "23:32:30"]
        for t in valid_times:
            self.assertTrue(check_time(t))

    def test_invalid_times(self):
        """Проверка некорректных значений времени"""
        invalid_times = ["24:00:00", "12:60:00", "12:30:99", "aa:bb:cc", "3A:24B:e7",
                         "123:45:67", "56:78:91", "99:99:99", "12:13:78", "33:33:33"]
        for t in invalid_times:
            self.assertFalse(check_time(t))

    def test_get_time(self):
        """Проверка извлечения всех корректных времён из текста"""
        text = "События: 12:30:45, 99:99:99, 00:00:00 и 23:59:59, а ещё 73:73:12 с 15:39:37."
        found = get_time(text)
        self.assertEqual(found, ["12:30:45", "00:00:00", "23:59:59", "15:39:37"])


if __name__ == "__main__":
    unittest.main()
