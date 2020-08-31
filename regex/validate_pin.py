"""
https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python

Given a string, return whether it is a 'valid PIN string' = exactly 4 digits or exactly 6 digits.

validate_pin("1234") == True
validate_pin("12345") == False
validate_pin("a234") == False
"""
import re


def validate_pin(pin: str) -> bool:
    return (len(pin) == 4 or len(pin) == 6) and contains_only_nums(pin)


def contains_only_nums(pin: str) -> bool:
    # First version iterates through pin's chars

    for char in pin:
        if not re.match(r'\d', char):
            return False
    return True

    # Here, for this version, I just create a bool from the return of checking the whole string at once
    # return bool(re.match(r'\d+', pin))


def validate_pin2(pin: str) -> bool:
    return (len(pin) == 4 or len(pin) == 6) and bool(re.match(r'\d+', pin))


def validate_pin3(pin: str) -> bool:
    '''buggy??'''
    return bool(re.match(r'\d{4,4}', pin) or re.match(r'\d{6,6}', pin))


def validate_pin4(pin):
    """
    Aha! This version bypasses using regex and just uses .isdigit()
    """
    return len(pin) in (4, 6) and pin.isdigit()


print(validate_pin3("1234"))
print(validate_pin3("12345"))
print(validate_pin3("a1234"))

print(validate_pin3("a12.34"))
