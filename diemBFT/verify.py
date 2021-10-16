import nacl.exceptions
from nacl.signing import SigningKey, VerifyKey

if __name__ == '__main__':
    # Generate a new signing key
    private_key = SigningKey.generate()

    signed_message = private_key.sign(b"qwerty")

    verify_key = private_key.verify_key
    #verify_key_bytes = verify_key.encode()

    #verify_key = VerifyKey(verify_key_bytes)

    try:
        verify_key.verify(signed_message)
        #verify_key.verify(signed_message.message, signed_message.signature)
    except nacl.exceptions.BadSignatureError:
        print('FORGED-1')

    forged = signed_message[:-1] + bytes([int(signed_message[-1]) ^ 1])

    try:
        verify_key.verify(forged)
    except nacl.exceptions.BadSignatureError:
        print('FORGED-2')