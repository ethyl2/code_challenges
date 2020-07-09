"""
From Kapil Sharma's lecture 06-18-2020

"Find the length of the longest non-repeating substring in a given array."

We assume that repeating means that it has more than one instance of an individual character.

"aefgaie" would result in 5, because longest non-repeating substring is "efgai".
(Another non-repeating substring is "aefg" but it is only 4 characters long.)
"""

# First way, with time O(n^3) and O(n) space.
# Note: I'm keeping track of the what the winning substring is, but it's not necessary,
# since we are only returning the winning length. So you can take the code to track that out, if you want.


def find_length(input_string):
    if input_string == None:
        return -1
    if len(input_string) == 0:
        return 0
    max_length = 1
    max_substring = input_string[0]
    length = len(input_string)
    for i in range(length):
        for j in range(i+1, length):
            substring = input_string[i:j+1]
            if is_all_unique(substring):
                substring_length = len(substring)
                if substring_length > max_length:
                    # print(substring)
                    max_substring = substring
                    max_length = substring_length

                # You can use this line below instead of the above block,
                # if you don't want to keep track of the winning substring:
                # max_length = max(max_length, j-i+1)
    print(max_substring)
    return max_length


def is_all_unique(input_substring):
    lookup = set()
    for char in input_substring:
        if char in lookup:
            return False
        else:
            lookup.add(char)
    return True


'''
print(find_length("aefgaie"))  # 5
print(find_length("aefgfie"))  # 4
print(find_length("aefgoie"))  # 6
print(find_length(None))  # -1
print(find_length(""))  # 0
print(find_length("aaaaaaaa"))  # 1
'''

# Second way that is more time efficient. O(n) time. O(n) space.


def find_length2(input_string):
    if input_string == None:
        return -1
    if len(input_string) == 0:
        return 0

    lookup = dict()
    left = 0
    right = 0
    max_length = 1
    length = len(input_string)

    # Iterate until right pointer reaches the end of the input_string
    while right < length - 1:
        c = input_string[right]
        if c not in lookup:
            lookup[c] = right
        else:
            # If c has been seen before,
            # move the left pointer to the right of the index where c was seen last.
            left = lookup[c] + 1
            # Update the value for c in the lookup dictionary to be its current index.
            lookup[c] = right
        right += 1
        max_length = max(max_length, right-left)

    return max_length


print(find_length2("aefgaie"))  # 5
print(find_length2("aefgfie"))  # 4
print(find_length2("aefgoie"))  # 6
print(find_length2(None))  # -1
print(find_length2(""))  # 0
print(find_length2("aaaaaaaa"))  # 1
