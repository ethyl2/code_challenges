"""
https://github.com/LambdaSchool/cs-module-project-hash-tables/tree/master/applications/crack_caesar

Find the key for the ciphertext in file ciphertext.txt. The file only contains uppercase letters and punctuation.
    Analyze the frequency of letters to figure it out.

Then decode it and show the plaintext.
All non-letters should pass through as-is.

"""

import sys
import os
most_used_to_least_used = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
                           'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']


with open(os.path.join(sys.path[0], 'ciphertext.txt')) as f:
    # Read in all the words in one go
    words = f.read()

# Make letter_count dictionary to see which chars are used the most
letter_count = {}
for char in words:
    if char.isupper():
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

# Now create the ciphertext key
ciphertext_key = {}
for index, entry in enumerate(sorted(letter_count.items(), key=lambda entry: -entry[1])):
    ciphertext_key[entry[0]] = most_used_to_least_used[index]


# Finally, decrypt the text
for char in words:

    if char.isupper():
        print(ciphertext_key[char], end='')

    else:
        print(char, end='')
