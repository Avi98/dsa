"""
Docstring for two_pointer_sliding.longest_nice_subarray

You are given an array nums consisting of positive integers.

We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

Return the length of the longest nice subarray.

A subarray is a contiguous part of an array.

Note that subarrays of length 1 are always considered nice.

Input: nums = [1,3,8,48,10]
Output: 3
Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
- 3 AND 8 = 0.
- 3 AND 48 = 0.
- 8 AND 48 = 0.
It can be proven that no longer nice subarray can be obtained, so we return 3.

https://leetcode.com/problems/longest-nice-subarray/description/
"""


def longest_nice_subarray(nums: list[int]):
    """
    Docstring for longest_nice_subarray
    - basic algo -
    1. curr & nums[i] == 0
        - update r pointer
    2. curr & nums[i] != 0
        - move l (shirk window)
        - unset l  using curr XOR with l

    :param nums: Description
    :type nums: list[int]
    """
    left = 0
    curr = 0

    res = 0

    for index, right in enumerate(nums):
        # print(f"{right} & {1} = {right & curr} ")
        while curr & right:
            curr = curr ^ nums[left]
            left += 1

        res = max(curr, index - left + 1)
        curr = curr ^ right

    return res


if __name__ == "__main__":
    curr = longest_nice_subarray([1, 3, 8, 48, 10])

    print(curr)
