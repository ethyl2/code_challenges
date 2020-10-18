"""
https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/more-conditional-structures

Given the following code:

temp = "5 degrees"
cel = 0
fahr = float(temp)
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)

Which line/lines should be surrounded by try block?
"""

temp = "5 degrees"
cel = 0
try:
    fahr = float(temp)
    cel = (fahr - 32.0) * 5.0 / 9.0

except:
    print('float conversion unsuccessful')

print(cel)
