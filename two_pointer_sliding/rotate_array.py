"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

"""


def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]

        left += 1
        right -= 1


def solution(nums: list[int], k: int):
    l, r = 0, len(nums) - 1
    k = k % len(nums)

    # 1. reverse the whole string
    reverse(nums, left=l, right=r)

    # 2. reverse the k els
    reverse(nums, left=l, right=k)

    # 3. reverse the rest of els
    reverse(nums, left=k, right=len(nums) - 1)

    return nums


if __name__ == "__main__":
    nums = solution([1, 2, 3, 4, 5, 6, 7], 3)
    print(nums)
