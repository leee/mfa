import unittest
import crc16
import os
import struct

class TestCrc16(unittest.TestCase):
    def test_checksum(self):
        bs = os.urandom(14)
        cs = crc16.get(bs)
        fc = ~cs & 0xffff
        bs = bs + struct.pack("<i", fc)[:2]
        self.assertTrue(crc16.verify(str(bs)))

if __name__ == '__main__':
    unittest.main()
