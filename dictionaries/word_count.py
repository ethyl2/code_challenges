"""
https://github.com/LambdaSchool/cs-module-project-hash-tables/tree/master/applications/word_count

This function takes a single string as an argument.
example:
Hello, my cat. And my cat doesn't say "hello" back.

It returns a dictionary of words and their counts:

{'hello': 2, 'my': 2, 'cat': 2, 'and': 1, "doesn't": 1, 'say': 1, 'back': 1}
Case should be ignored. Output keys must be lowercase.

Key order in the dictionary doesn't matter.

Split the strings into words on any whitespace.

Ignore each of the following characters:

" : ; , . - + = / \ | [ ] { } ( ) * ^ &
If the input contains no ignored characters, return an empty dictionary. <- should be 'only', not 'no' ignored characters, I think!
"""
import re


def word_count(s):
    word_counts = {}

    for word in re.split(', |_|-|!|\r|\t|\n|\s', s):
        formatted_word = re.sub(
            r'[\"\:\;\,\.\-\+\=\/\\\|\[\]\{\}\(\)\*\^\&]', '', word).lower()
        if formatted_word in word_counts:
            word_counts[formatted_word] += 1
        else:
            if len(formatted_word) > 0:
                word_counts[formatted_word] = 1

    return word_counts


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('a a\ra\na\ta \t\r\n'))
