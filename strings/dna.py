"""
https://www.codewars.com/kata/554e4a2f232cdd87d9000038

Given a DNA strand string, return its complementary strand.

Examples:
DNA_strand ("ATTGC") # return "TAACG"

DNA_strand ("GTAT") # return "CATA"
"""


def DNA_strand(dna: str) -> str:
    bases = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([bases[current] for current in dna])


print(DNA_strand("ATTGC"))
print(DNA_strand("GTAT"))
