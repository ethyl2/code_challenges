"""
https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting&isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Given d <- number of trailing days needed before bank sends notifications
Given expenditure <- arr of amount spent each day

Bank sends notification if amount spent that day is >= 2 times the median spending for trailing num of days.

Print num of times the client will receive a notification (during the days included in expenditure arr)

If d=3, expenditure=[10,20,30,40,50]
Day 4: median of [10,20,30] is 20 and 40 is spent.
40 >= 20 * 2 so notification is sent.

Day 5: median of [20, 30, 40] is 30. 50 is spent.
50 is not >= 30 * 2 so no notification.

Print 1.

The median of a list of numbers can be found by arranging all the numbers from smallest to greatest.
If there is an odd number of numbers, the middle one is picked. 
If there is an even number of numbers, median is then defined to be the average of the two middle values.
"""
import statistics
import sys
import os


def find_median(nums):
    nums.sort()
    if len(nums) % 2 == 1:
        # odd length
        return nums[len(nums)//2]
    else:
        # even length
        mid_num1 = nums[len(nums)//2]
        mid_num2 = nums[(len(nums)//2) - 1]
        return (mid_num1 + mid_num2)/2


def activityNotifications(expenditure, d):
    # Initialize var for num of notifications
    num_notifications = 0
    # Loop through expenditure, starting at index d
    #   Calculate median of past d days
    #   Compare median to 2 * that day's expenditure
    #   If >= then increment counter.
    for i in range(d, len(expenditure)):
        print("i is: " + str(i))
        print(expenditure[i-3:i])
        current_median = statistics.median(expenditure[i-3:i])
        # Or to use my function:
        # current_median = find_median(expenditure[i-3:i])
        print("median: " + str(current_median) + ' * 2 = ' +
              str(current_median * 2) + " versus " + str(expenditure[i]))
        # print("day_amount: ", str(expenditure[i]))
        if (current_median * 2) <= expenditure[i]:
            num_notifications += 1
    print(num_notifications)
    return(num_notifications)


# print(find_median([10, 20, 30]))
# activityNotifications([10, 20, 30, 40, 50], 3)  # 1
# activityNotifications([1, 2, 3, 4, 4], 4)  # 0
# activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5)  # 2
activityNotifications([0, 82, 180, 55, 168, 41, 179, 59,
                       139, 71, 6, 12, 135, 139, 73, 157, 4, 74, 195], 14)
'''
with open(os.path.join(sys.path[0], 'large_case.txt'), 'r') as f:
    nums = f.read().split(" ")

activityNotifications(nums, 10000)  # 633
'''
