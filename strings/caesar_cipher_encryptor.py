"""
From algo expert

Given a non-empty string of lowercase letters and a non-negative input representing a key,
write a function that returns a new string obtained by shifting every letter in the input string by 
k positions in the alphabet, where k is the ky.

Note: letters should wrap around the alphabet. Example 'z' shifted by 1 returns 'a'

Example: string = 'xyz', key = 2 -> 'zab'
"""


import string

# O(n) time for iterating through the string
# O(n) space for output string creation


def encryptor(s, key):
    key = key % 26
    output = ''
    for char in s:
        shifted_num_value = ord(char) + key
        if shifted_num_value > 122:
            shifted_num_value = shifted_num_value % 122 + 96
        output += chr(shifted_num_value)
    return output


# print(encryptor('xyz', 2))


# This version uses an alphabet list instead of ascii values.
# O(n) time for iterating through the string, where n is the length of the string + O(m) for each call of .index(), where m is the length of the alphabet.
# So overall O(n + m*n) -> O(m*n) time
# O(m) time for creating the alphabet list, where m is the length of the alphabet. A one-time thing, so if I were encrypting multiple strings,
#   I'd move the alphabet list creation outside of the function.

# Space O(m) for alphabet list creation.
# Space O(n) for output string creation.
def encryptor2(s, key):
    alphabet = list(string.ascii_lowercase)

    key = key % 26
    output = ''
    for char in s:
        shifted_num_value = alphabet.index(char) + key
        if shifted_num_value >= 26:
            shifted_num_value = shifted_num_value % 26
        output += alphabet[shifted_num_value]
    return output

# print(encryptor2('xyz', 2))


# Third version makes a dictionary of the alphabet for encryption. And then a reversed version to lookup chars by the indices.
# O(n) to make each dictionary, but O(1) for every lookup after that. For multiple encryptions, I would move the dictionaries'
#   creation outside of the function.

# Space O(2m) -> O(m) for dictionaries' creation
# Space O(n) for output string creation.
def encryptor3(s, key):
    alphabet = {value: key for (
        key, value) in enumerate(string.ascii_lowercase)}
    reversed_dict = {value: key for (key, value) in alphabet.items()}

    key = key % 26
    output = ''

    for char in s:
        shifted_num_value = alphabet[char] + key
        if shifted_num_value >= 26:
            shifted_num_value = shifted_num_value % 26
        output += reversed_dict[shifted_num_value]
    return output


print(encryptor3('xyz', 2))
