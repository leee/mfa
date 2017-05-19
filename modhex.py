import sys

hexadecimal_bytes = b"0123456789abcdef"
modhex_bytes      = b"cbdefghijklnrtuv"
hexadecimal_unicode = hexadecimal_bytes.decode('ascii')
modhex_unicode = modhex_bytes.decode('ascii')

# Yubico YubiKey Manual v3.4 s6.2: "Modified Hexadecimal (Modhex) encoding"

if sys.version_info >= (3,0):
    maketrans = bytes.maketrans
else:
    import string
    maketrans = string.maketrans

trans_table_encode_bytes = maketrans(hexadecimal_bytes, modhex_bytes)
trans_table_decode_bytes = maketrans(modhex_bytes, hexadecimal_bytes)
trans_table_encode_unicode = trans_table_encode_bytes[:128].decode('ascii')
trans_table_decode_unicode = trans_table_decode_bytes[:128].decode('ascii')

def by_string_type(typedstring, bytesversion, unicodeversion):
    if isinstance(typedstring, bytes):
        return bytesversion
    else:
        return unicodeversion

def is_hexadecimal(s):
    return len(s.strip(by_string_type(s, hexadecimal_bytes, hexadecimal_unicode))) == 0

def is_modhex(s):
    return len(s.strip(by_string_type(s, modhex_bytes, modhex_unicode))) == 0

def encode(s):
    return s.translate(by_string_type(s, trans_table_encode_bytes, trans_table_encode_unicode))

def decode(s):
    return s.translate(by_string_type(s, trans_table_decode_bytes, trans_table_decode_unicode))

