"""
https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python

Given parameters
1.h, the height of a building, where a child is dropping a ball out of a window from that height.
2. bounce, the amount the ball will bounce back up after it is dropped.
3. window, the height of the window that that mom is at and will see the ball pass by.

Conditions:
1. h > 0
2. 0 < bounce < 1
3. window < h

If conditions are met, return num times mom will see the ball.
Else, return -1.

Sample tests:
test.assert_equals(bouncingBall(3, 0.66, 1.5), 3)
test.assert_equals(bouncingBall(30, 0.66, 1.5), 15)
"""

# My iterative solution


def bouncingBall(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    else:
        num_times = 1
        ball_height = h*bounce

        while ball_height > window:
            num_times += 2
            ball_height = ball_height*bounce

        return num_times

# This cleans up the code a bit, by reusing h, instead of introducing a separate variable ball_height.


def bouncingBall3(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    else:
        num_times = 1
        h *= bounce

        while h > window:
            num_times += 2
            h *= bounce
        return num_times

# This is my recursive attempt. It passes some of the cases.


def bouncingBall2(h, bounce, window, num_times=1, initial_check=True):
    if initial_check and (h <= 0 or bounce <= 0 or bounce >= 1 or window >= h):
        print('initial_check')
        return -1
    if h < window:
        return num_times
    return bouncingBall2(h*bounce, bounce, window, num_times + 1, False)


print(bouncingBall3(3, 0.66, 1.5))
print(bouncingBall3(30, 0.66, 1.5))
print(bouncingBall3(3, 1, 1.5))
