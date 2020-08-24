"""
https://www.codewars.com/kata/546f922b54af40e1e90001da

Given a string, replace each letter with its position in the alphabet.
If char isn't a letter, don't include it in the return string.

Example:
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)
"""
import string


def alphabet_position(text: str) -> str:
    alphabet = string.ascii_lowercase
    alphabet_dict = {}
    output_list = []
    for i in range(len(alphabet)):
        alphabet_dict[alphabet[i]] = str(i+1)
    for char in text.lower():
        if char in alphabet_dict:
            output_list.append(alphabet_dict[char])
    return ' '.join(output_list)


print(alphabet_position("The sunset sets at twelve o' clock."))
