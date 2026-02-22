"""

Search Element in a Rotated Sorted Array


Problem Statement: Given an integer array nums, sorted in ascending order (with distinct values) and a target value k.
The array is rotated at some pivot point that is unknown. Find the index at which k is present and if k is not present return -1.

Examples
Input:nums = [4, 5, 6, 7, 0, 1, 2], k = 0
Output :4
Explanation : Here, the target is 0. We can see that 0 is present in the given rotated sorted array, nums. Thus, we get output as 4, which is the index at which 0 is present in the array.

Input: nums = [4, 5, 6, 7, 0, 1, 2], k = 3
Output :-1
Explanation :Here, the target is 3. Since 3 is not present in the given rotated sorted array. Thus, we get the output as -1.
"""

import math


def rotated_array(nums: list[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = math.ceil((low + high) / 2)

        if nums[mid] == target:
            return mid
        # if left is sorted
        if nums[low] < nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


if __name__ == "__main__":
    res = rotated_array([4, 5, 6, 7, 0, 1, 2], target=0)
    print(res)
