"""
https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer (32-bit signed integer range: [−2^31,  2^31 − 1]), reverse its digits
Returns 0 when the reversed integer overflows

Examples:
123 => 321
-123 => -321
120 => 21
"""


class Solution:

    # First approach converts int into a list, then reverses it before converting it back to an int.
    def reverse(self, x: int) -> int:
        is_neg = x < 0
        int_list = list(str(abs(x)))
        int_list.reverse()
        reversed_string = ''.join(int_list)
        if is_neg:
            reversed_string = '-' + reversed_string
        output = int(reversed_string)
        if output > 2**31 or output < -2**31:
            return 0
        return output

    # Second approach uses a doubly-linked-list.
    # It's not any better, because I ended up using a string to get the digits.

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None

    def reverse2(self, x: int) -> int:
        class Node:

            def __init__(self, value):
                self.value = value
                self.next = None
                self.prev = None

        is_neg = x < 0
        int_list = list(str(abs(x)))
        abs_x = abs(x)
        prev = None
        curr = Node(int_list[0])
        for i in range(1, len(int_list)):
            curr.next = Node(int_list[i])
            curr.prev = prev
            prev = curr
            curr = curr.next
        curr.prev = prev

        output = []

        while curr:
            output.append(curr.value)
            curr = curr.prev
        output_string = ''.join(output)
        if is_neg:
            output_string = '-' + output_string
        output_int = int(output_string)
        if output_int > 2**31 or output_int < -2**31:
            return 0
        return(output_int)

    # This approach uses modulus to get the digits. It is more space efficient.
    def reverse3(self, x: int) -> int:
        is_neg = x < 0
        x = abs(x)
        output = []
        while x > 0:
            curr_digit = x % 10
            output.append(curr_digit)
            x //= 10
        output_int = sum(digit * 10**i for i, digit in enumerate(output[::-1]))
        if is_neg:
            output_int = -output_int
        if output_int > 2**31 or output_int < -2**31:
            return 0
        return(output_int)


s = Solution()
print(s.reverse3(123))
print(s.reverse3(-123))
print(s.reverse3(120))
