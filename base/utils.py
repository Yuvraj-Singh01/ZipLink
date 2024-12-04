import string

BASE62_ALPHABET = string.digits + string.ascii_letters

def encode_to_base62(number):
    if number == 0:
        return BASE62_ALPHABET[0]
    result = []
    while number > 0:
        result.append(BASE62_ALPHABET[number % 62])
        number //= 62
    return ''.join(reversed(result))
