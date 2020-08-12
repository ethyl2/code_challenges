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


# TODO: analyze which words can follow other words
# Your code here
lookup = {}
starts = set()
stops = set()

for i in range(len(words_list)-1):

    if words_list[i] not in lookup:
        lookup[words_list[i]] = [words_list[i+1]]
        if words_list[i][0].isupper() or (words_list[i][0] == '"' and len(words_list[i]) > 1 and words_list[i][1].isupper()):
            starts.add(words_list[i])
        if words_list[i][-1] in '.?!' or (len(words_list[i]) > 1 and words_list[i][-1] == '"' and words_list[i][-2] in '.?!'):
            stops.add(words_list[i])
    else:
        lookup[words_list[i]].append(words_list[i+1])

# Add the last word to starts and stops, if it qualifies for either/both:
if words_list[i+1][0].isupper() or (words_list[i+1][0] == '"' and len(words_list[i+1]) > 1 and words_list[i+1][1].isupper):
    starts.add(words_list[i])
if words_list[i+1][-1] in '.?!' or (len(words_list[i+1]) > 1 and words_list[i+1][-1] == '"' and words_list[i+1][-2] in '.?!'):
    stops.add(words_list[i+1])

# print(lookup)
# print(starts)
# print(stops)


# TODO: construct 5 random sentences
# Your code here


for i in range(5):
    first_word = random.choice(list(starts))
    print(first_word, end=' ')
    next_word = random.choice(lookup[first_word])

    while next_word not in stops:
        print(next_word, end=' ')
        next_word = random.choice(lookup[next_word])
    print(next_word)
