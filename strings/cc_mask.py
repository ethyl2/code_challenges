"""
https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python

Given a string consisting of a cc number,
return a string in which all but the last four characters are changed into #

maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""
"""


def maskify(cc: str) -> str:
    if len(cc) < 4:
        return cc
    return '#' * (len(cc)-4) + cc[-4:]


print(maskify("4556364607935616"))
print(maskify("64607935616"))

print(maskify("1"))

print(maskify(""))
