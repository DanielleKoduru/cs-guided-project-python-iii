"""
Demonstration #2

Given a non-empty array of integers `nums`, every element appears twice except except for one. Write a function that finds the element that only appears once.

Examples:

- single_number([3,3,2]) -> 2
- single_number([5,2,3,2,3]) -> 5
- single_number([10]) -> 10
"""


def single_number(nums):
    for num in nums:
        # count the number of times num appears
        count = nums.count(num)
        if count == 1:
            return num


print(single_number([3, 3, 2]))
print(single_number([5, 2, 3, 2, 3]))
print(single_number([10]))
