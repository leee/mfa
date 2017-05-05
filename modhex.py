import string
import sys

hexadecimal = b"0123456789abcdef"
modhex      = b"cbdefghijklnrtuv"

# Yubico YubiKey Manual v3.4 s6.2: "Modified Hexadecimal (Modhex) encoding"
if sys.version_info >= (3,0):
    trans_table_encode = bytes.maketrans(hexadecimal, modhex)
    trans_table_decode = bytes.maketrans(modhex, hexadecimal)
else:
    trans_table_encode = string.maketrans(hexadecimal, modhex)
    trans_table_decode = string.maketrans(modhex, hexadecimal)
'''
def is_hexadecimal(s):
    s = interop(s)
    return '' == s.strip(hexadecimal.decode('utf-8'))

def is_modhex(s):
    s = interop(s)
    return '' == s.strip(modhex.decode('utf-8'))
'''

def encode(s):
    s = interop_trans(s)
    return s.translate(trans_table_encode)

def decode(s):
    s = interop_trans(s)
    return s.translate(trans_table_decode)

'''
def translate(s):
    if is_hexadecimal(s) and not is_modhex(s):
        return encode(s)
    elif not is_hexadecimal(s) and is_modhex(s):
        return decode(s)
    else:
        raise ValueError('A modhex.translate failed because', s,
            'is not hexadecimal or Modhex and therefore not encode/decodable.')

def interop(s):
    if sys.version_info < (3,0):
        return s.encode('utf-8')
    else:
        return s.encode( )
'''

def interop_trans(s):
    if sys.version_info < (3,0):
        return s.encode('utf-8')
    else:
        return s
