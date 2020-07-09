"""
From codesignal: https://app.codesignal.com/interview-practice/task/yM4uWYeQTHzYewW9H/description

crypt is arr of 3 strings containing uppercase English chars.
solution is a nested arr with entries of [letter, num as string]

Once crypt is decoded using solution, if it makes a valid math equation, return True.
If any of the addends or sum has a leading 0 (besides 0 itself), return False.
"""


def is_crypt_solution(crypt, solution):
    # Convert solution to dict
    # Decode each entry of crypt
    # If have a leading zero, return False
    # Check to see if addend1 + addend2 == sum
    # If so, return True. Else False.

    decoder = {}
    for entry in solution:
        decoder[entry[0]] = entry[1]

    decoded_words = []
    for word in crypt:
        decoded = decode(decoder, word)
        if len(decoded) > 1 and decoded[0] == '0':
            return False
        decoded_words.append(int(decoded))

    if decoded_words[0] + decoded_words[1] == decoded_words[2]:
        return True
    return False


def decode(decoder, word):
    decoded = ''
    for i, char in enumerate(word):
        decoded += decoder[char]
    return decoded


print(is_crypt_solution(["SEND", "MORE", "MONEY"], [['O', '0'],
                                                    ['M', '1'],
                                                    ['Y', '2'],
                                                    ['E', '5'],
                                                    ['N', '6'],
                                                    ['D', '7'],
                                                    ['R', '8'],
                                                    ['S', '9']]))

print(is_crypt_solution(["TEN", "TWO", "ONE"], [['O', '1'],
                                                ['T', '0'],
                                                ['W', '9'],
                                                ['E', '5'],
                                                ['N', '4']]))

print(is_crypt_solution(["A",
                         "A",
                         "A"], [["A", "0"]]))

print(is_crypt_solution(["AA",
                         "AA",
                         "AA"], [["A", "0"]]))

'''
# First and less dry solution:
    addend1 = ''
    for i, char in enumerate(crypt[0]):
        addend1 += decoder[char]
    # print(addend1)
    if len(addend1) > 1 and addend1[0] == '0':
        return False
    addend1 = int(addend1)

    addend2 = ''
    for i, char in enumerate(crypt[1]):
        addend2 += decoder[char]
    # print(addend2)
    if len(addend2) > 1 and addend2[0] == '0':
        return False
    addend2 = int(addend2)

    total = ''
    for i, char in enumerate(crypt[2]):
        total += decoder[char]
    # print(total)
    if len(total) > 1 and total[0] == '0':
        return False
    total = int(total)

    # Then check if addend1 + addend2 == total
    '''
