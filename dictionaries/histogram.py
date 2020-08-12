"""
https://github.com/LambdaSchool/cs-module-project-hash-tables/tree/master/applications/histo

Print a histogram showing the word count for each word, one hash mark for every occurrence of the word.

Output will be first ordered by the number of words, then by the word (alphabetically).

The hash marks should be left justified two spaces after the longest word.

Case should be ignored, and all output forced to lowercase.

Split the strings into words on any whitespace.

Ignore each of the following characters:

" : ; , . - + = / \ | [ ] { } ( ) * ^ &
If the input contains no ignored characters, print nothing. <- Should be modified to say, 'only' ignored characters, I think!

Sample output (truncated):

the              ################################################
and              ####################################
of               ###################################
a                ########################
with             #################
to               ################
robin            #############
he               ############
his              ############
that             ############
in               ###########
at               ##########
good             ##########
i                ##########
as               #########
for              #######
green            #######
thou             #######
upon             #######
ale              ######
all              ######
bow              ######
"""
import sys
import os
import re


def histo(text_file):
    with open(os.path.join(sys.path[0], text_file)) as f:
        # Read in all the words in one go
        words = f.read()

    longest_word_length = 0
    words_dict = {}
    for word in words.split():
        formatted_word = re.sub(
            r'[\"\:\;\,\.\-\+\=\/\\\|\[\]\{\}\(\)\*\^\&]', '', word).lower()

        if formatted_word in words_dict:
            words_dict[formatted_word] += 1
        else:
            words_dict[formatted_word] = 1

        longest_word_length = max(len(formatted_word), longest_word_length)

    for word, count in sorted(words_dict.items(), key=lambda entry: (-entry[1], entry[0])):
        print(word + ' ' * (longest_word_length + 2 - len(word)) + '#' * count)


histo('robin.txt')
# histo('input.txt')
