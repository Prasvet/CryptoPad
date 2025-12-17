import unittest
from core.cipher import (
    reverse_text,
    swap_adjacent,
    shift_by_one,
    unshift_by_one,
    shift_by_position,
    unshift_by_position
)


class TestCipherAlgorithms(unittest.TestCase):

    # 1. Тест инвертирования текста (алгоритм 0)
    def test_reverse_text(self):
        self.assertEqual(reverse_text("hello"), "olleh")
        self.assertEqual(reverse_text(""), "")  # Пустая строка
        self.assertEqual(reverse_text("a"), "a")  # Один символ
        self.assertEqual(reverse_text("12345"), "54321")  # Цифры
        self.assertEqual(reverse_text("A b C"), "C b A")  # Пробелы и регистр

    # 2. Тест перестановки соседних (алгоритм 1)
    def test_swap_adjacent(self):
        self.assertEqual(swap_adjacent("abcd"), "badc")
        self.assertEqual(swap_adjacent("abc"), "bac")  # Нечётная длина
        self.assertEqual(swap_adjacent("a"), "a")  # Один символ
        self.assertEqual(swap_adjacent(""), "")  # Пустая строка
        self.assertEqual(swap_adjacent("XY"), "YX")  # Два символа

    # 3. Тест сдвига на 1 (алгоритм 2) и обратного преобразования
    def test_shift_unshift_one(self):
        # Базовый тест
        text = "ABC"
        encrypted = shift_by_one(text)
        decrypted = unshift_by_one(encrypted)
        self.assertEqual(decrypted, text)

        # Разные символы
        self.assertEqual(unshift_by_one("bcd"), "abc")
        self.assertEqual(shift_by_one("xyz"), "yza")  # Учёт переполнения
        self.assertEqual(unshift_by_one("yza"), "xyz")

        # Крайние случаи
        self.assertEqual(unshift_by_one("", shift=1), "")
        self.assertEqual(shift_by_one("", shift=1), "")

    # 4. Тест позиционного сдвига (алгоритм 3) и обратного преобразования
    def test_shift_unshift_position(self):
        text = "abc"
        base = 33

        # Прямое и обратное преобразование
        encrypted = shift_by_position(text, base=base)
        decrypted = unshift_by_position(encrypted, base=base)
        self.assertEqual(decrypted, text)

        # Подробный пример: "abc" → "ace"
        example = "ace"
        result = unshift_by_position(example, base=base)
        self.assertEqual(result, "abc")

        # Длинная строка (проверка цикла по модулю 33)
        long_text = "a" * 35  # 35 символов
        encrypted_long = shift_by_position(long_text, base=base)
        decrypted_long = unshift_by_position(encrypted_long, base=base)
        self.assertEqual(decrypted_long, long_text)

    # 5. Тест крайних случаев для позиционного сдвига
    def test_edge_cases_position(self):
        # Пустая строка
        self.assertEqual(unshift_by_position("", base=33), "")
        self.assertEqual(shift_by_position("", base=33), "")

        # Один символ
        self.assertEqual(unshift_by_position("a", base=33), "a")
        self.assertEqual(shift_by_position("a", base=33), "a")

        # Два символа
        encrypted = shift_by_position("ab", base=33)
        decrypted = unshift_by_position(encrypted, base=33)
        self.assertEqual(decrypted, "ab")

    # 6. Тест разных значений base
    def test_different_base_values(self):
        text = "abc"
        # base = 10
        encrypted_10 = shift_by_position(text, base=10)
        decrypted_10 = unshift_by_position(encrypted_10, base=10)
        self.assertEqual(decrypted_10, text)

        # base = 5
        encrypted_5 = shift_by_position(text, base=5)
        decrypted_5 = unshift_by_position(encrypted_5, base=5)
        self.assertEqual(decrypted_5, text)


    # 7. Тест устойчивости к спецсимволам
    def test_special_characters(self):
        text = "Hello, мир! 123@"
        encrypted = shift_by_one(text)
        decrypted = unshift_by_one(encrypted)
        self.assertEqual(decrypted, text)

        # Позиционный сдвиг со спецсимволами
        encrypted_pos = shift_by_position(text, base=33)
        decrypted_pos = unshift_by_position(encrypted_pos, base=33)
        self.assertEqual(decrypted_pos, text)



if __name__ == '__main__':
    unittest.main()
