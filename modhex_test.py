import unittest
import modhex

class TestModhex(unittest.TestCase):
    def test_is_hexadecimal(self):
        self.assertTrue(modhex.is_hexadecimal(modhex.hexadecimal))

    def test_is_not_hexadecimal(self):
        self.assertFalse(modhex.is_hexadecimal(modhex.modhex))

    def test_is_modhex(self):
        self.assertTrue(modhex.is_modhex(modhex.modhex))

    def test_is_not_modhex(self):
        self.assertFalse(modhex.is_modhex(modhex.hexadecimal))

    def test_encode(self):
        self.assertEqual(modhex.encode(modhex.hexadecimal), modhex.modhex)

    def test_decode(self):
        self.assertEqual(modhex.decode(modhex.modhex), modhex.hexadecimal)

    def test_translate_encode(self):
        self.assertEqual(modhex.translate(modhex.hexadecimal), modhex.modhex)

    def test_translate_decode(self):
        self.assertEqual(modhex.translate(modhex.modhex), modhex.hexadecimal)

    def test_translate_nothing(self):
        self.assertIsNone(modhex.translate("mopqswxyz"))

if __name__ == '__main__':
    unittest.main()
