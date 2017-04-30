import string

# Yubico YubiKey Manual v3.4 s6.2: "Modified Hexadecimal (Modhex) encoding"
hexadecimal = '0123456789abcdef'
modhex      = 'cbdefghijklnrtuv'

trans_table_encode = string.maketrans(hexadecimal, modhex)
trans_table_decode = string.maketrans(modhex, hexadecimal)

def is_hexadecimal(s):
    return '' == s.strip(hexadecimal)

def is_modhex(s):
    return '' == s.strip(modhex)

def encode(s):
    return s.translate(trans_table_encode)

def decode(s):
    return s.translate(trans_table_decode)

def translate(s):
    if is_hexadecimal(s) and not is_modhex(s):
        return encode(s)
    elif not is_hexadecimal(s) and is_modhex(s):
        return decode(s)
    else:
        raise ValueError('A modhex.translate failed because', s,
            'is not hexadecimal or Modhex and therefore not encode/decodable.')
