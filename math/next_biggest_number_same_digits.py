"""
https://www.codewars.com/kata/55983863da40caa2c900004e

Given a positive integer, return the next biggest number that can be formed by rearranging its digits, or -1 if that can't be done.

Approach:
Go backwards through the digits.
When a digit is greater than the one in front of it (let's call the digit in front D),
    swap D with the digit to the right of D that is the smallest digit that is bigger than D.
Then sort the digits to the right of where D used to be, to make the smallest number possible. (Ascending)

1733951
9 is greater than 3, so
swap the right-most 3 with 5, since 5>3 and 5 is smaller than 9.
1735931
Next, sort 931 ascending.
1735139

"""


def next_bigger(num: int) -> int:
    num_list = [int(char) for char in str(num)]
    for i in range(len(num_list)-1, 0, -1):
        if num_list[i] > num_list[i-1]:
            # Swap num_list[i-1] with whatever is to the right and is the smallest number bigger than num_list[i-1]
            current_num_index = i-1
            swap_index = find_next_biggest(current_num_index, num_list)
            num_list[i-1], num_list[swap_index] = num_list[swap_index], num_list[i-1]
            # Then arrange the nums to the right of current_num_index to be the smallest value possible.
            sort_part(current_num_index + 1, num_list)
            nums_as_strings = [str(digit) for digit in num_list]
            return int(''.join(nums_as_strings))
    return -1


def find_next_biggest(current_num_index, num_list):

    current_winning_index = current_num_index + 1

    current_num = num_list[current_num_index]
    # print('current_num: ', current_num)
    # print('looking at sublist: ', num_list[current_num_index:])
    for i in range(current_num_index + 1, len(num_list)):

        if num_list[i] < num_list[current_winning_index] and num_list[i] > current_num:

            current_winning_index = i
            # print('current winning value: ', num_list[i])
    # print('ready to return: ',
    #       num_list[current_winning_index], 'at index: ', current_winning_index)

    return current_winning_index


def sort_part(current_num_index, num_list):
    did_swap = True
    while did_swap:
        did_swap = False
        for i in range(current_num_index, len(num_list) - 1):
            if num_list[i] > num_list[i+1]:
                did_swap = True
                num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
    return num_list


# print(next_bigger(12))

# print(next_bigger(513)) # 531
# print(next_bigger(2017))  # 2071
# print(next_bigger(414) == 441)
# print(next_bigger(144) == 414)

# print(next_bigger(9))
# print(next_bigger(111))
# print(next_bigger(531))


print(next_bigger(1733951))  # 1735139
print(next_bigger(1733951) == 1735139)
# print(find_next_biggest(676))

# print(next_bigger(5358253))  # 5358325
# print(next_bigger(5358253) == 5358325)

# print(next_bigger(1674))  # 1746

# print(next_bigger(44687))  # 44768
