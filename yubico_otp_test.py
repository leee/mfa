import unittest
import yubico_otp
import os
import random

class TestYubicoOTP(unittest.TestCase):
    def test_conversion_from_bytestring(self):
        bs = os.urandom(16)
        hexa = yubico_otp.bytestring_to_hexadecimal(bs)
        bs2 = yubico_otp.hexadecimal_to_bytestring(hexa)
        self.assertEqual(bs, bs2)

    def test_conversion_from_hexadecimal(self):
        hexa = '0123456789abcdef'
        bs = yubico_otp.hexadecimal_to_bytestring(hexa)
        hexa2 = yubico_otp.bytestring_to_hexadecimal(bs)
        self.assertEqual(hexa, hexa2)

    def test_crypto(self):
        data = yubico_otp.bytestring_to_hexadecimal(os.urandom(16))
        key = yubico_otp.bytestring_to_hexadecimal(os.urandom(16))
        data_e = yubico_otp.encrypt(data, key)
        data2 = yubico_otp.decrypt(data_e, key)

    def test_otp(self):
        pub = 'cbdefghijklnrtuv'
        uid = yubico_otp.bytestring_to_hexadecimal(os.urandom(6))
        useCtr = random.randint(1, 32767)
        tstp = random.randint(0, 16777215)
        sessionCtr = random.randint(0, 255)
        key = yubico_otp.bytestring_to_hexadecimal(os.urandom(16))
        password = yubico_otp.generate(pub, uid, useCtr, tstp, sessionCtr, key)
        pub2, uid2, useCtr2, tstp2, sessionCtr2, rnd2 = \
                                            yubico_otp.degenerate(password, key)
        self.assertEqual(pub, pub2)
        self.assertEqual(uid, uid2)

if __name__ == '__main__':
    unittest.main()
