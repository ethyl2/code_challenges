"""
https://leetcode.com/problems/word-ladder/

Andrew Candela's lecture 09-15-2020

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0
"""
from typing import List, Dict
from collections import deque, defaultdict


def preprocessor(begin_word: str, end_word: str, word_list: List[str]) -> Dict[str, str]:
    """
    Return a dictionary consisting of intermediate strings 
    (which are words with one wildcard character taking the place of one character) as the keys,
    with the values as lists of the words that fit the intermediate string.

    Example: if begin_word is 'hit', end_word is 'hag', and word_list is ['hat']:
    {
        '*it': ['hit'], 
        'h*t': ['hit', 'hat'], 
        'hi*': ['hit'], 
        '*ag': ['hag'], 
        'h*g': ['hag'], 
        'ha*': ['hag', 'hat'], 
        '*at': ['hat']}
    """
    out_map = defaultdict(list)
    for intermed_string in create_intermed_strings(begin_word):
        out_map[intermed_string].append(begin_word)
    for intermed_string in create_intermed_strings(end_word):
        out_map[intermed_string].append(end_word)
    for word in word_list:
        for intermed_string in create_intermed_strings(word):
            out_map[intermed_string].append(word)
    return out_map


def create_intermed_strings(word: int) -> List[str]:
    """
    This takes a word and returns a list of strings in which one character is replaced by a wildcard character.

    Example:
    'cog' -> ['*og', 'c*g', 'co*']
    """
    intermed_strings = []
    for i in range(len(word)):
        intermed_string = f"{word[:i]}*{word[i+1:]}"
        intermed_strings.append(intermed_string)
    return intermed_strings


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Do a BFS using the adjacency list created with preprocessor to get the shortest path length
        between beginWord and endWord.
        """
        # edge case
        if endWord not in wordList:
            return 0

        # Initialize variables
        queue = deque()
        level = 2
        visited = set([])
        adjacency_list = preprocessor(beginWord, endWord, wordList)

        # Push the first items onto the queue

        beginning_intermed_strings = create_intermed_strings(beginWord)

        for intermed_string in beginning_intermed_strings:
            for word in adjacency_list[intermed_string]:
                if word == endWord:
                    return level
                queue.append((word, level))

        # BST as long as there are items in the queue
        while queue:
            current_word, level = queue.popleft()
            visited.add(current_word)
            level += 1
            current_intermed_strings = create_intermed_strings(current_word)
            for intermed_string in current_intermed_strings:
                for word in adjacency_list[intermed_string]:
                    if word == endWord:
                        return level
                    if word not in visited:
                        queue.append((word, level))

        return 0


# print(create_intermed_strings("cog"))
# preprocessor("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])

s = Solution()
print(s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
