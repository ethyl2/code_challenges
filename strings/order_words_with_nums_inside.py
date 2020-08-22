"""
https://www.codewars.com/kata/55c45be3b2079eccff00010f

Given a string consisting of words. Each word has letters and one single number.
Return a string where each input word is at the index indicated by the number inside the word.

Examples:
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
"""
import re


def order(sentence: str) -> str:

    output = [''] * len(sentence.split())
    for word in sentence.split():
        index = int(re.findall(r'\d', word)[0]) - 1
        output[index] = word
    return ' '.join(output)


print(order("is2 Thi1s T4est 3a"))
