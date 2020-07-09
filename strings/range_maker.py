"""
https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/python
Given an sorted array of ints (I'm assuming they are unique?)
Return a string in which the ints are formatted of a comma separated elements of either an individual int,
or a range of ints num1-num3, inclusive. A range must span at least 3 nums.

Example:
solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8,
         9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
"""
# keep a min variable for the beginning of a range and max for end.
# Loop through every int and see if it is a loner, or should be part of a range.
#   If args[i] + 1 == args[i+1] and min == None, then min = args[i]
#   Elif args[i] + 1 == args[i+1], max = args[i]
#   Elif min != None, add min-max to return_string*, and reset min and max to None.
#       If args[i] + 1 != args[i+1], add args[i] to return_string
#       else, set args[i] to be min.
# Add to the return_string accordingly.
# * Do check to make sure range is at least 3 ints, if not, add individual elements to the return_string instead.


def solution(args):
    return_string = ''
    min = max = None
    for i in range(len(args) - 1):
        if args[i] + 1 == args[i+1]:
            if not min:
                min = args[i]
            max = args[i+1]

        else:
            if max:
                if max-min > 1:
                    return_string += f'{str(min)}-{str(max)},'
                else:
                    return_string += f'{str(min)},{str(max)},'
                min = max = None
            else:
                return_string += f'{str(args[i])},'

    # Taking care of the end.
    if max and max-min > 1:
        return_string = return_string + f'{str(min)}-{str(max)}'
    elif max:
        return_string += f'{str(min)},{str(max)}'
    else:
        return_string += f'{str(args[-1])}'
    return return_string

# Here's someone's version, which uses an array to store results initially,
# and then converts it to a string at the end.


def solution2(args):
    out = []
    beg = end = args[0]

    for n in args[1:] + [""]:
        if n != end + 1:
            if end == beg:
                out.append(str(beg))
            elif end == beg + 1:
                out.extend([str(beg), str(end)])
            else:
                out.append(str(beg) + "-" + str(end))
            beg = n
        end = n

    return ",".join(out)


print(solution2([-6, -3, -2, -1, 0, 1, 3, 4, 5,
                 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
