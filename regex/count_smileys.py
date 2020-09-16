"""
https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python

Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

Rules for a smiling face:

Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]

countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

If array is empty, return 0.
Order of face will always be the same.
"""
from typing import List
import re


def count_smileys(arr: List[str]) -> int:
    """
    Time O(n) where n is length of arr
    Space O(1)
    """
    if len(arr) < 1:
        return 0
    count = 0
    for face in arr:
        # print(face)
        if bool(re.match(r'[\:;]{1}[\-\~]{0,1}[\)D]{1}', face)):
            # print(re.match(r'[\:;]{1}[\-\~]{0,1}[\)D]{1}', face))
            count += 1
    return count


def count_smileys_concise(arr: List[str]) -> int:
    """
    Another person's implementation. Turns the list into an string,
    then uses findall() on that string.
    Turning the result into a list makes it possible to return the length of that list.
    So this version is more concise, but uses more space. O(n) where n is length of arr.
    """
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))


print(count_smileys([':)', ';(', ';}', ':-D']))  # 2
print(count_smileys([';D', ':-(', ':-)', ';~)']))  # 3
print(count_smileys([';]', ':[', ';*', ':$', ';-D']))  # 1
