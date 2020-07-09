"""
https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting&isFullScreen=true&h_r=next-challenge&h_v=zen

Given an array of n Player objects, write a comparator that sorts them in order of decreasing score.
If same score, sort alphabetically ascending by name.

Create a Checker class the implements the Comparator interface,
then write an int compare(Playera, Playerb) method implementing the Comparator.compare() method.

comparator returns -1 if a<b, 0 if a == b, 1 if a>b                                                                        

"""
from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return "f{self.name} {int(self.score)}"

    def comparator(a, b):
        if a.score > b.score:
            return -1
        if a.score < b.score:
            return 1
        if a.score == b.score:
            if a.name < b.name:
                return -1
            else:
                return 1


n = int(input())
