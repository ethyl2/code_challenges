"""
What does 'continue' do in the middle of a loop?

Does it:
    - Skip to the code directly after the loop?
    - Skip to the next line in the code?
    - Skip to the next iteration of the loop?
    - Skip the next block of code?
"""

nums = [7, 3, -1, 8, -9]
positive_nums = []

for num in nums:
    if num < 0:  # skips to the next iteration
        continue
    positive_nums.append(num)

print(positive_nums)  # 7,3,8

for i in range(10):
    if i == 3:  # skips if i is 3
        continue
    print(i)
