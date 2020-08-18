"""
https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

Given a string of one or more words,
Return a string of the same words, but if a word has 5 or more letters, it should be reversed.

Examples:
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
spinWords( "This is a test") => returns "This is a test"
spinWords( "This is another test" )=> returns "This is rehtona test"
"""


def spin_words(sentence: str) -> str:
    output = []
    for word in sentence.split():
        if len(word) >= 5:
            output.append(''.join(reversed([char for char in word])))
        else:
            output.append(word)
    return ' '.join(output)


print(spin_words("Hey fellow warriors"))
