import re

"""
https://www.codewars.com/kata/551dc350bf4e526099000ae5/python

Get original song: words separated by a space,
given string where 0 or more "DUB"s are at the beginning,
                at least 1 between any pair of neighboring words,
                and 0 or more at the end.
        The input consists of a single non-empty string, 
                consisting only of uppercase English letters, 
                the string's length doesn't exceed 200 characters.

Example:
input: "WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"
output: "WE ARE THE CHAMPIONS MY FRIEND"
"""


def song_decoder(song):
    return re.sub(r'(WUB)+', ' ', song).strip()


def song_decoder2(song):
    return " ".join(song.replace('WUB', ' ').split())


print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))
