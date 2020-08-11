"""
It's like the Fibonacci Sequence, but a lot more computationally expensive and a lot less useful.

exps(x, y, z) =
     if x <= 0: y + z
     if x >  0: exps(x-1,y+1,z) + exps(x-2,y+2,z*2) + exps(x-3,y+3,z*3)
x, y, and z are all greater than or equal to zero.

This will be tested on inputs as large as:

x = 150
y = 400
z = 800
Use a hashtable to make sure your solution completes before the universe ends.
"""
lookup = {}


def expensive_seq(x, y, z):
    global lookup
    if (x, y, z) in lookup:
        return lookup[(x, y, z)]
    elif x <= 0:
        return y + z
    else:
        if (x-1, y+1, z) in lookup:
            first = lookup[(x-1, y+1, z)]
        else:
            first = expensive_seq(x-1, y+1, z)
            lookup[(x-1, y+1, z)] = first

        if (x-2, y+2, z*2) in lookup:
            second = lookup[(x-2, y+2, z*2)]
        else:
            second = expensive_seq(x-2, y+2, z*2)
            lookup[(x-2, y+2, z*2)] = second

        if (x-3, y+3, z*3) in lookup:
            third = lookup[(x-3, y+3, z*3)]
        else:
            third = expensive_seq(x-3, y+3, z*3)
            lookup[(x-3, y+3, z*3)] = third

        result = first + second + third
        lookup[(x, y, z)] = result
        return result


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
