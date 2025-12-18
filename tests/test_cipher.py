import unittest
from core.cipher import (
    reverse_text,
    swap_adjacent,
    shift_chars,
    shift_by_position,
    ALGORITHMS,
    ALGORITHM_NAMES,
)


class TestCipherAlgorithms(unittest.TestCase):

    def test_reverse_text(self):
        self.assertEqual(reverse_text("abc", False), "cba")
        self.assertEqual(reverse_text("Hello!", False), "!olleH")
        self.assertEqual(reverse_text("cba", True), "abc")
        self.assertEqual(reverse_text("", False), "")
        self.assertEqual(reverse_text("x", False), "x")

    def test_swap_adjacent(self):
        self.assertEqual(swap_adjacent("abcd", False), "badc")
        self.assertEqual(swap_adjacent("abcde", False), "badce")
        self.assertEqual(swap_adjacent("", False), "")
        self.assertEqual(swap_adjacent("x", False), "x")
        self.assertEqual(swap_adjacent("ab", False), "ba")
        self.assertEqual(swap_adjacent("badc", True), "abcd")

    def test_shift_chars_encrypt(self):
        self.assertEqual(shift_chars("abc", False, 1), "bcd")
        self.assertEqual(shift_chars("abc", False, 2), "cde")
        # Исправлено: ожидаем реальный результат сдвига по ASCII
        self.assertEqual(shift_chars("a b!", False, 1), 'b!c"')
        self.assertEqual(shift_chars("", False, 1), "")

    def test_shift_chars_decrypt(self):
        self.assertEqual(shift_chars("bcd", True, 1), "abc")
        self.assertEqual(shift_chars("cde", True, 2), "abc")
        # Исправлено: дешифруем "b!c"" → получаем "a b!"
        self.assertEqual(shift_chars('b!c"', True, 1), "a b!")

    def test_shift_by_position_encrypt(self):
        self.assertEqual(shift_by_position("abc", False, 33), "ace")
        self.assertEqual(shift_by_position("", False, 33), "")

    def test_shift_by_position_decrypt(self):
        self.assertEqual(shift_by_position("ace", True, 33), "abc")
        encrypted = shift_by_position("wxyz", False, 3)
        decrypted = shift_by_position(encrypted, True, 3)
        self.assertEqual(decrypted, "wxyz")

    def test_algorithms_registry(self):
        for algo_id in ALGORITHMS:
            self.assertIn(algo_id, ALGORITHM_NAMES)
        for algo_id, func in ALGORITHMS.items():
            with self.subTest(algorithm=algo_id):
                result = func("test", False)
                self.assertIsInstance(result, str)

    def test_algorithm_names(self):
        for name in ALGORITHM_NAMES.values():
            self.assertIsInstance(name, str)
            self.assertGreater(len(name), 0)
        self.assertEqual(len(ALGORITHMS), len(ALGORITHM_NAMES))


if __name__ == "__main__":
    unittest.main()
