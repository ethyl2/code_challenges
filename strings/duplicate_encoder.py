"""
https://www.codewars.com/kata/54b42f9314d9229fd6000d9c
Given a string,
return a string where "(" is located for each char that appears only once in the input & ')' if char appears more than once. 
Increase char counts no matter whether char is upper or lowercase.

Examples:
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
"""


def duplicate_encode(word: str) -> str:
    singles = set()
    duplicates = set()
    word = word.lower()
    output = ''
    for char in word:
        if char in singles:
            duplicates.add(char)
        singles.add(char)

    for char in word:
        if char in duplicates:
            output += ')'
        else:
            output += '('
    return output


print(duplicate_encode("din"))
print(duplicate_encode("recede"))
print(duplicate_encode(")())())"))
print(duplicate_encode("Success"))
print(duplicate_encode("(( @"))
