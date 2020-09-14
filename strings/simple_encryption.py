"""
https://www.codewars.com/kata/57814d79a56c88e3e0000786/train/python

For encrypt(), Given a string, a int n, return a string with 2 parts concatenated: The first part contains every 2nd char. The second part contains the rest.
Do it n times.

Example:
"This is a test!", 1 -> "hsi  etTi sats!"

"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"

For decrypt(), do the opposite.
"""


def encrypt(text, n):

    if not text or len(text) == 0 or n <= 0:
        return text

    for _ in range(n):
        first, second = '', ''
        has_odd_length = len(text) % 2 == 1
        for i in range(0, len(text) - 1, 2):
            first += text[i+1]
            second += text[i]
        very_last = text[-1]
        text = first + second
        if has_odd_length:
            text += very_last

    return text


def decrypt2(text, n):
    """
    Another's solution. More concise! Using[i:i+1] keep index errors from happening!
    """
    if text in ("", None):
        return text

    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i+1] + a[i:i+1] for i in range(ndx + 1))
    return text


def encrypt2(text, n):
    """
    Another person's solution. I like how they used the 3rd parameter for skipping every other char.
    """
    for i in range(n):
        text = text[1::2] + text[::2]
    return text


print(encrypt2("This is a test!", 1))
print(encrypt2("This is a test!", 2))
print(encrypt2("This kata is very interesting!", 1))


def decrypt(encrypted_text, n):

    if n <= 0 or not encrypted_text or len(encrypted_text) == 0:
        return encrypted_text

    for _ in range(n):
        decrypted_text = ''
        for i in range(len(encrypted_text)//2):
            decrypted_text += encrypted_text[i + len(encrypted_text)//2]
            decrypted_text += encrypted_text[i]

        if len(encrypted_text) % 2 == 1:
            decrypted_text += encrypted_text[-1]

        encrypted_text = decrypted_text
    return decrypted_text


print(decrypt2("hskt svr neetn!Ti aai eyitrsig", 1))
print(decrypt2(" Tah itse sits!", 3))
