import unittest
from caesar_cipher import caesar_cipher


class TestCaesarCipher(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(caesar_cipher("HELLO", 3), "KHOOR")

    def test_decrypt(self):
        self.assertEqual(caesar_cipher("KHOOR", -3), "HELLO")

    def test_lowercase(self):
        self.assertEqual(caesar_cipher("hello", 3), "khoor")

    def test_mixed_case(self):
        self.assertEqual(caesar_cipher("Hello", 3), "Khoor")

    def test_spaces_and_symbols(self):
        self.assertEqual(
            caesar_cipher("Hello, World!", 3),
            "Khoor, Zruog!"
        )

    def test_alphabet_wrap(self):
        self.assertEqual(caesar_cipher("XYZ", 3), "ABC")

    def test_large_shift(self):
        self.assertEqual(caesar_cipher("ABC", 29), "DEF")

    def test_negative_shift(self):
        self.assertEqual(caesar_cipher("ABC", -3), "XYZ")

    def test_empty_message(self):
        self.assertEqual(caesar_cipher("", 3), "")

    def test_full_rotation(self):
        self.assertEqual(caesar_cipher("HELLO", 26), "HELLO")


if __name__ == "__main__":
    unittest.main()