"""
https://github.com/LambdaSchool/cs-module-project-hash-tables/tree/master/applications/markov

1. Read the file input.txt and split it into words.
Don't worry about changing punctuation or capitalization. For example, a "word" might be "Hello,. Just leave it all in there.

2. Analyze the text, building up the dataset of which words can follow particular words.

3. Choose a random "start word" to begin. Start words are words that begin with a capital, or a " followed by a capital.

4. Loop through:

Print the word.
If it's a "stop word", stop. Stop words are words that end in any of the punctuation .?!, or that punctuation followed by a ".
Else randomly choose a word that can follow this one.

Stretch goal: Make sure there is always a close quote for an opening quote in the sentence.
"""

import random
import os
import sys

with open(os.path.join(sys.path[0], 'input.txt')) as f:
    # Read in all the words in one go
    words = f.read()

'''
# Small test input:
words = '"Cats and "dogs and birds and fish dogs!" birds.'
'''
words_list = words.split()
# print(words_list)


# analyze which words can follow other words

lookup = {}
starts = set()
stops = set()

for i in range(len(words_list)-1):

    if words_list[i] not in lookup:
        lookup[words_list[i]] = [words_list[i+1]]
        # Check to see if the word should be considered a start or stop
        if (words_list[i][0].isupper() and words_list[i][-1] != '"') or (words_list[i][0] == '"' and len(words_list[i]) > 1 and words_list[i][1].isupper()):
            starts.add(words_list[i])
        if words_list[i][-1] in '.?!' or (len(words_list[i]) > 1 and words_list[i][-1] == '"' and words_list[i][-2] in '.?!'):
            stops.add(words_list[i])
    else:
        lookup[words_list[i]].append(words_list[i+1])

# Add the last word to starts and stops, if it qualifies for either/both:
if (words_list[i+1][0].isupper() and words_list[i][-1] != '"') or (words_list[i+1][0] == '"' and len(words_list[i+1]) > 1 and words_list[i+1][1].isupper):
    starts.add(words_list[i])
if words_list[i+1][-1] in '.?!' or (len(words_list[i+1]) > 1 and words_list[i+1][-1] == '"' and words_list[i+1][-2] in '.?!'):
    stops.add(words_list[i+1])

# print(lookup)
# print(starts)
# print(stops)


# construct 5 random sentences


for i in range(5):
    num_opening_quotes = 0
    num_closing_quotes = 0

    first_word = random.choice(list(starts))
    if first_word[0] == '"':
        num_opening_quotes += 1
    if first_word[-1] == '"':
        num_closing_quotes += 1
    print(first_word, end=' ')

    next_word = random.choice(lookup[first_word])
    if next_word[0] == '"':
        num_opening_quotes += 1
    if next_word[-1] == '"':
        num_closing_quotes += 1

    while next_word not in stops:
        print(next_word, end=' ')
        next_word = random.choice(lookup[next_word])
        if next_word[0] == '"':
            num_opening_quotes += 1
        if next_word[-1] == '"':
            num_closing_quotes += 1

    if num_opening_quotes < num_closing_quotes and next_word[-1] == '"':
        print(next_word[:-1], end='')
    else:
        print(next_word, end='')
    if num_opening_quotes > num_closing_quotes:
        print('"')

    print('\n')
