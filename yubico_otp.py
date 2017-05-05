# Yubico YubiKey Manual v3.4 s6.1: "The Yubico OTP generation algorithm"
import modhex
import os
from Crypto.Cipher import AES
import binascii
import crc16
import struct
import sys

#           (mod, hex,    int,  int,        int, hex, hex     )
def generate(pub, uid, useCtr, tstp, sessionCtr, key, rnd=None):
    if rnd is None:
        # we assume os.urandom() to be a CSPRNG
        rnd = bytestring_to_hexadecimal(os.urandom(2))
    otp = generate_otp(uid, useCtr, tstp, sessionCtr, rnd)
    otp_e = encrypt(otp, key)
    return pub + modhex.encode(otp_e)

#                modhex, hex)
def degenerate(password, key):
    # last 32 chars of password is always otp, with rest of prefix being pub
    pub = password[:-32]
    otp_e = modhex.decode(password[-32:])
    otp = decrypt(otp_e, key)
    uid, useCtr, tstp, sessionCtr, rnd = degenerate_otp(otp)
    return pub, uid, useCtr, tstp, sessionCtr, rnd

#          (hex, hex)
def encrypt(otp, key):
    c = AES.new(hexadecimal_to_bytestring(key), AES.MODE_ECB)
    otp_e = c.encrypt(hexadecimal_to_bytestring(otp))
    return bytestring_to_hexadecimal(otp_e)

#          ( hex, hex)
def decrypt(otp_e, key):
    c = AES.new(hexadecimal_to_bytestring(key), AES.MODE_ECB)
    otp = c.decrypt(hexadecimal_to_bytestring(otp_e))
    return bytestring_to_hexadecimal(otp)

#               (hex,    int,  int,        int, hex)
def generate_otp(uid, useCtr, tstp, sessionCtr, rnd):
    uid_bs = hexadecimal_to_bytestring(uid)
    useCtr_bs = struct.pack("<i", useCtr)[:2]
    tstp_bs = struct.pack("<i", tstp)[:3]
    sessionCtr_bs = struct.pack(">i", sessionCtr)[3:]
    rnd_bs = hexadecimal_to_bytestring(rnd)
    bs = uid_bs + useCtr_bs + tstp_bs + sessionCtr_bs + rnd_bs
    checksum = crc16.get(bs)
    checksum_first_complement = ~checksum & 0xffff
    crc = struct.pack("<i", checksum_first_complement)[:2]
    bs = bs + crc
    return bytestring_to_hexadecimal(bs)

def degenerate_otp(otp):
    otp_bs = hexadecimal_to_bytestring(otp)
    uid = bytestring_to_hexadecimal(otp_bs[0:6])
    useCtr = struct.unpack("<i", otp_bs[6:8] + b"\x00\x00")
    tstp = struct.unpack("<i", otp_bs[8:11] + b"\x00")
    sessionCtr = struct.unpack("<i", int_to_bytestring(otp_bs[11]) + b"\x00\x00\x00")
    rnd = bytestring_to_hexadecimal(otp_bs[12:14])
    return uid, useCtr, tstp, sessionCtr, rnd

# why is python 2 and 3 interoperability hard
def int_to_bytestring(i):
    if sys.version_info >= (3,0):
        return i.to_bytes(1, 'little')
    else:
        return i

def bytestring_to_hexadecimal(bs):
    return binascii.hexlify(bs).decode('utf-8')

def hexadecimal_to_bytestring(hexa):
    return binascii.unhexlify(hexa)
