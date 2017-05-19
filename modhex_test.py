import unittest
import modhex

hexexamplestr = u'1234cdef'
hexexamplebytes = b'1234cdef'
modhexexamplestr = u'bdefrtuv'
modhexexamplebytes = b'bdefrtuv'

class TestModhex(unittest.TestCase):
    def test_encode_str(self):
        self.assertEqual(modhex.encode(hexexamplestr), modhexexamplestr)

    def test_encode_bytes(self):
        self.assertEqual(modhex.encode(hexexamplebytes), modhexexamplebytes)

    def test_decode_str(self):
        self.assertEqual(modhex.decode(modhexexamplestr), hexexamplestr)

    def test_decode_bytes(self):
        self.assertEqual(modhex.decode(modhexexamplebytes), hexexamplebytes)

    def test_is_hexadecimal_str(self):
        self.assertTrue(modhex.is_hexadecimal(hexexamplestr))

    def test_is_hexadecimal_bytes(self):
        self.assertTrue(modhex.is_hexadecimal(hexexamplebytes))

    def test_is_not_hexadecimal_bytes(self):
        self.assertFalse(modhex.is_hexadecimal(modhexexamplebytes))

    def test_is_not_hexadecimal_str(self):
        self.assertFalse(modhex.is_hexadecimal(modhexexamplestr))

    def test_is_modhex_bytes(self):
        self.assertTrue(modhex.is_modhex(modhexexamplebytes))

    def test_is_modhex_str(self):
        self.assertTrue(modhex.is_modhex(modhexexamplestr))

    def test_is_not_modhex_bytes(self):
        self.assertFalse(modhex.is_modhex(hexexamplebytes))

    def test_is_not_modhex_str(self):
        self.assertFalse(modhex.is_modhex(hexexamplestr))

    #def test_translate_encode(self):
    #    self.assertEqual(modhex.translate(hexexamplebytes), modhexexamplebytes)

    #def test_translate_decode(self):
    #    self.assertEqual(modhex.translate(modhexexamplebytes), hexexamplebytes)

    #def test_translate_bad(self):
    #    self.assertRaises(ValueError, modhex.translate, b'mopqswxyz')


if __name__ == '__main__':
    unittest.main()
