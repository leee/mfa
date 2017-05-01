# Yubico YubiKey Manual v3.4 s6.3: "CRC calculation and verification"
# Literally copied the ISO13239 CRC16 algo provided, down to the bitwise ops.

def get(bs):
    crc = 0xffff
    for b in bs:
        crc ^= ord(b)
        for i in range(8):
            j = crc & 1
            crc >>= 1
            if j:
                crc ^= 0x8408
    return crc

def verify(bs):
    return get(bs) == 0xf0b8
