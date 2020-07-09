def handle_justification(line, l):
    print(line)
    output = ""
    n_chars = 0

    for word in line:
        n_chars += len(word)

    # default spaces is the "normal" spaces needed between each word 
    default_spaces = len(line) - 1
    padding_needed = l - n_chars

    # if the line only has one word, then left-justify the line 
    if default_spaces == 0:
        return line[0] + (" " * padding_needed)

    # figure out how much padding needs to be added to each default space 
    padding_per_space = padding_needed // default_spaces
    # also figure out remaining padding that needs to be added to each
    # default space starting from the left-most default space 
    remaining_padding = padding_needed % default_spaces

    for i, word in enumerate(line):
        spaces = padding_per_space

        # add on any remaining spaces we need to reach the length limit
        if i < remaining_padding:
            spaces += 1

        # if this is the last word in the line, don't add any spaces to it
        if i == default_spaces:
            spaces = 0

        spaces = " " * spaces
        output += (word + spaces)

    return output

def textJustification(words, l):
    rv = []
    line = []
    n_chars = 0

    for word in words:
        # add in a space for each word after the first
        if n_chars > 0:
            n_chars += 1
        n_chars += len(word)

        # once we've overshot the length limit, add the
        # justified line to our result 
        # reset the line and our n_chars counter
        if n_chars > l:
            justified_string = handle_justification(line, l)
            rv.append(justified_string)
            n_chars = len(word)
            line = []

        line.append(word)

    # special handling for the last line
    if len(line) > 0:
        string = " ".join(line)
        string += (" " * (l - len(string)))
        rv.append(string)

    return rv
