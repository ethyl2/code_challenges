"""
https://www.youtube.com/watch?v=gxGygQyGNFk&feature=youtu.be
Given a array of strings and a line length,
put the strings in greedily, with equal spaces if possible.
If not possible, more space on left than on right.
If a line has just one word or is last line, put on left.

from codesignal.com
words <- arr of strings
l <- line length

words: ["This", "is", "an", "example", "of", "text", "justification"]
l: 16

output:["This    is    an",
        "example  of text",
        "justification.  "]
"""


def text_justification(words, l):
    # Initialize var for char count
    char_count = 0
    # Initialize var to hold current line's text
    current_line = []
    # Initialize var to hold arr of lines
    lines_arr = []
    for word in words:
        # See if adding num of chars to char count would make it be longer than l
        if len(word) + char_count > l:
            # Time to format line and then add to lines_arr.
            lines_arr.append(formatLine(current_line, l))
            # Reset current_line and char_count.
            current_line = []
            char_count = 0

        # Add word to current line
        current_line.append(word)

        # Increase char count.
        char_count += len(word)
        # If char count < l (that's not a one), increase char_count to add a space to current line
        if char_count < l:
            char_count += 1

    if lines_arr[-1] != current_line:
        # Need to format last line and add it.
        chars_in_line = 0
        end_string = ''
        for word in current_line:
            chars_in_line += (len(word) + 1)
            end_string += (word + ' ')
        spaces_for_end = l - chars_in_line
        end_string += (' ' * spaces_for_end)

        # Chop off the last space if not needed.
        if len(end_string) > l:
            end_string = end_string[:-1]
        lines_arr.append(end_string)

    print(lines_arr)
    return(lines_arr)


def formatLine(current_line, l):
    # Format current_line into a justified string.
    # Find out how many spaces are needed
    chars_in_current_line = 0
    for current_word in current_line:
        chars_in_current_line += len(current_word)
    # print(chars_in_current_line)
    num_spaces_needed = l - chars_in_current_line
    # print(num_spaces_needed)

    # Find out how many space places are needed (len(current_line) -1)
    space_places = len(current_line) - 1
    if space_places:
        # Figure out how many spaces are needed in each space_place
        num_for_each_place = num_spaces_needed//space_places
        # See if those divide evenly.
        remainder = num_for_each_place % space_places
    else:
        # No spaces needed in this case.
        num_for_each_place = 0

    # Convert the arr to a string
    current_string = ''
    for i in range(len(current_line)-1):
        current_string += (current_line[i] +
                           (' ' * num_for_each_place))
        if remainder:
            current_string += ' '
            remainder -= 1

    current_string += current_line[-1]
    return current_string


text_justification(["This", "is", "an", "example",
                    "of", "text", "justification."], 16)
text_justification(["This", "is", "an", "example",
                    ], 6)
