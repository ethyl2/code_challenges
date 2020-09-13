"""
https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

Given an int that is a number of seconds, return a string.
If int is 0, return 'now'.
Otherwise,
return string in an ordered combination of years, days, hours, minutes, and seconds.

Examples:
format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
"""


def format_duration(seconds: int) -> str:
    if seconds == 0:
        return 'now'
    time_amounts = {'years': 0, 'days': 0,
                    'hours': 0, 'minutes': 0, 'seconds': 0}
    output = ''

    if seconds >= 31536000:
        time_amounts['years'] = seconds//31536000
        output += str(time_amounts['years'])
        output += " years, " if time_amounts['years'] > 1 else " year, "
        seconds = seconds % 31536000
    if seconds >= 86400:
        time_amounts['days'] = seconds//86400
        output += str(time_amounts['days'])
        output += " days, " if time_amounts['days'] > 1 else " day, "
        seconds = seconds % 86400
    if seconds >= 3600:
        time_amounts['hours'] = seconds//3600
        output += str(time_amounts['hours'])
        output += " hours, " if time_amounts['hours'] > 1 else " hour, "
        seconds = seconds % 3600
    if seconds >= 60:
        time_amounts['minutes'] = seconds//60
        output += str(time_amounts['minutes'])
        output += " minutes, " if time_amounts['minutes'] > 1 else " minute, "
        seconds = seconds % 60
    time_amounts['seconds'] = seconds

    # Find left-most comma and replace it with ' and'

    num_of_digits = sum(c.isdigit() for c in output)
    if num_of_digits > 1:
        output = ' and'.join(output.rsplit(',', 1))

    else:
        output = output[:-2]

    # Handle seconds
    if num_of_digits == 1 and time_amounts['seconds'] > 0:
        output += ' and '
    if time_amounts['seconds'] == 1:
        output += str(time_amounts['seconds']) + ' second'
    elif time_amounts['seconds'] > 1:
        output += str(time_amounts['seconds']) + ' seconds'
    elif num_of_digits > 1 and time_amounts['seconds'] == 0:
        output = output[:-5]
        output = ' and'.join(output.rsplit(',', 1))

    # print(seconds, time_amounts)
    return output


print(format_duration(31536100))
print(format_duration(62))
print(format_duration(3662))
print(format_duration(120))
print(format_duration(1))
print(format_duration(132030240))
