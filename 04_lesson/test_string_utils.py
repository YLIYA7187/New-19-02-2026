import unittest
from string_utils import StringUtils  # исправлено: string_utils вместо string_utilis


class TestStringUtils(unittest.TestCase):
    def setUp(self):
        self.utils = StringUtils()

    # Тесты для capitalize
    def test_capitalize_normal(self):
        """Позитивный тест: обычная строка"""
        self.assertEqual(self.utils.capitalize("skypro"), "Skypro")

    def test_capitalize_empty_string(self):
        """Негативный тест: пустая строка"""
        self.assertEqual(self.utils.capitalize(""), "")

    def test_capitalize_single_char(self):
        """Позитивный тест: один символ"""
        self.assertEqual(self.utils.capitalize("a"), "A")

    def test_capitalize_already_capitalized(self):
        """Позитивный тест: уже с заглавной буквы"""
        self.assertEqual(self.utils.capitalize("Skypro"), "Skypro")

    def test_capitalize_numbers(self):
        """Позитивный тест: строка с цифрами"""
        self.assertEqual(self.utils.capitalize("123abc"), "123abc")

    # Тесты для trim
    def test_trim_leading_spaces(self):
        """Позитивный тест: пробелы в начале"""
        self.assertEqual(self.utils.trim("   skypro"), "skypro")

    def test_trim_no_spaces(self):
        """Позитивный тест: нет пробелов в начале"""
        self.assertEqual(self.utils.trim("skypro"), "skypro")

    def test_trim_empty_string(self):
        """Негативный тест: пустая строка"""
        self.assertEqual(self.utils.trim(""), "")

    def test_trim_only_spaces(self):
        """Негативный тест: только пробелы"""
        self.assertEqual(self.utils.trim("   "), "")

    def test_capitalize_none(self):
        """Негативный тест: передача None вместо строки"""
        with self.assertRaises(AttributeError):
            self.utils.capitalize(None)

    def test_trim_none(self):
        """Негативный тест: передача None вместо строки"""
        with self.assertRaises(AttributeError):
            self.utils.trim(None)
