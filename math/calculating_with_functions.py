"""
https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python

This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3

Looks like the number functions must allow either 0 or 1 parameters. The 1 parameter is an operation function invoked.
Looks like the operation functions must take a number function invoked as a parameter.
"""


def zero(*operation_function_invocation):
    if operation_function_invocation:
        if (operation_function_invocation[0][0] == '//' and operation_function_invocation[0][1] == '0'):
            return 'No division by zero allowed'
        return eval('0' + operation_function_invocation[0][0] + operation_function_invocation[0][1])
    return '0'


def one(*operation_function_invocation):
    if operation_function_invocation:
        if (operation_function_invocation[0][0] == '//' and operation_function_invocation[0][1] == '0'):
            return 'No division by zero allowed'
        return eval('1' + operation_function_invocation[0][0] + operation_function_invocation[0][1])
    else:
        return '1'


def two(*operation_function_invocation):
    if operation_function_invocation:
        if (operation_function_invocation[0][0] == '//' and operation_function_invocation[0][1] == '0'):
            return 'No division by zero allowed'
        return eval('2' + operation_function_invocation[0][0] + operation_function_invocation[0][1])
    else:
        return '2'


def three(*operation_function_invocation):
    if operation_function_invocation:
        if (operation_function_invocation[0][0] == '//' and operation_function_invocation[0][1] == '0'):
            return 'No division by zero allowed'
        return eval('3' + operation_function_invocation[0][0] + operation_function_invocation[0][1])
    else:
        return '3'


def four(*operation_function_invocation):
    if operation_function_invocation:

        if (operation_function_invocation[0][0] == '//' and operation_function_invocation[0][1] == '0'):
            return 'No division by zero allowed'
        return eval('4' + operation_function_invocation[0][0] + operation_function_invocation[0][1])
    else:
        return '4'


def five(*operation_function_invocation):
    if operation_function_invocation:
        if (operation_function_invocation[0][0] == '//' and operation_function_invocation[0][1] == '0'):
            return 'No division by zero allowed'
        return eval('5' + operation_function_invocation[0][0] + operation_function_invocation[0][1])
    else:
        return '5'


def six(*operation_function_invocation):
    if operation_function_invocation:
        if (operation_function_invocation[0][0] == '//' and operation_function_invocation[0][1] == '0'):
            return 'No division by zero allowed'
        return eval('6' + operation_function_invocation[0][0] + operation_function_invocation[0][1])
    else:
        return '6'


def seven(*operation_function_invocation):
    if operation_function_invocation:
        if (operation_function_invocation[0][0] == '//' and operation_function_invocation[0][1] == '0'):
            return 'No division by zero allowed'
        return eval('7' + operation_function_invocation[0][0] + operation_function_invocation[0][1])
    else:
        return '7'


def eight(*operation_function_invocation):
    if operation_function_invocation:
        if (operation_function_invocation[0][0] == '//' and operation_function_invocation[0][1] == '0'):
            return 'No division by zero allowed'
        return eval('8' + operation_function_invocation[0][0] + operation_function_invocation[0][1])
    else:
        return '8'


def nine(*operation_function_invocation):
    if operation_function_invocation:
        if (operation_function_invocation[0][0] == '//' and operation_function_invocation[0][1] == '0'):
            return 'No division by zero allowed'
        return eval('9' + operation_function_invocation[0][0] + operation_function_invocation[0][1])
    else:
        return '9'


def plus(number_function_invocation):
    return '+', number_function_invocation


def minus(number_function_invocation):
    return '-', number_function_invocation


def times(number_function_invocation):
    return '*', number_function_invocation


def divided_by(number_function_invocation):
    return '//', number_function_invocation


def checkForDivisionByZero(operator, string_num):
    if (operator == '//' and string_num == '0'):
        return True


# print(one(plus(one())))
# print(nine(plus(two())))
# print(zero(plus(four())))
# print(four(plus(zero())))
# print(nine(times(two())))
# print(nine(divided_by(two())))
# print(nine(minus(two())))
# print(zero(divided_by(four())))
print(five(divided_by(zero())))


'''
# Another person's solution:
def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x/y
"""
