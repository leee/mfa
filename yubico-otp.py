# TODO: function naming scheme here could be better, probably

def generate_otp_token(uid, useCtr, tstp, sessionCtr, rnd, crc):
    # TODO; throw exceptions/errors when any of these values are garbage?
    # Yubico YubiKey Manual v3.4 s6.1: "The Yubico OTP generation algorithm"
    pass

def generate_password(token, key, pub):
    # takes in otp token, aes128 key, does the crypto, public id, modhex
    # TODO: public id validation? see Yubico YubiKey Manual v3.4 s5.4.1
    pass

def generate_otp(pub, uid, useCtr, tstp, sessionCtr, rnd, crc, key):
    return generate_password(
        generate_otp_token(uid, useCtr, tstp, sessionCtr, rnd, crc), key, pub)
