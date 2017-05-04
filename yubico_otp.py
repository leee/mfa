# Yubico YubiKey Manual v3.4 s6.1: "The Yubico OTP generation algorithm"
import modhex
import os
from Crypto.Cipher import AES
import binascii
import crc16

#           (mod, hex,    int,  int,        int, hex)
def generate(pub, uid, useCtr, tstp, sessionCtr, key):
    return generate(pub, uid, useCtr, tstp, sessionCtr, os.urandom(2), key)

#           (mod, hex,    int,  int,        int, str, hex)
def generate(pub, uid, useCtr, tstp, sessionCtr, rnd, key):
    otp = generate_otp(uid, useCtr, tstp, sessionCtr, rnd)
    otp_e = encrypt(otp, key)
    return pub + modhex.to_modhex(otp_e)

#          (hex, hex)
def encrypt(otp, key):
    c = AES.new(hexadecimal_to_bytestring(key), AES.MODE_ECB)
    otp_e = c.encrypt(hexadecimal_to_bytestring(otp))
    return bytestring_to_hexadecimal(otp_e)

#               (  hex,        int,      int,            int, str)
def generate_otp(uid_h, useCtr_int, tstp_int, sessionCtr_int, rnd):
    uid = hexadecimal_to_bytestring(uid_h)
    useCtr = struct.pack("<i", useCtr_int)[:2]
    tstp = struct.pack("<i", tstp_int)[:3]
    sessionCtr = struct.pack(">i", sessionCtr_int)[3:]
    bs = uid + useCtr + tstp + sessionCtr + rnd
    checksum = crc16.get(bs)
    checksum_first_complement = ~checksum & 0xffff
    crc = struct.pack("<i", checksum_first_complement)[:2]
    bs = bs + crc
    return bytestring_to_hexadecimal(bs)

def bytestring_to_hexadecimal(bs):
    return binascii.hexlify(bs).decode('utf-8')

def hexadecimal_to_bytestring(hexa):
    return binascii.unhexlify(hexa)
