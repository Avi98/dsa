"""
Docstring for sorting.bubble_sort

Bubble Sort Algorithm .

Problem Statement: Given an array of N integers, write a program to implement the Bubble Sorting algorithm.

Example 1:
Input: N = 5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting we get 1,2,3,4,5


Example 2:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting we get 9,13,20,24,46,52

"""

import pprint


def bubble_sort(nums: list[int], length) -> list[int]:
    for i in range(length - 1, 0, -1):
        for j in range(i - 1):
            if nums[j] > nums[j + 1]:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]

    return nums


if __name__ == "__main__":
    sort = bubble_sort([5, 4, 3, 2, 1], 5)
    pprint.pprint(sort)
