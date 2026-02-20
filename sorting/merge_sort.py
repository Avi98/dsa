"""
Docstring for sorting.merge_sort
Merge sort
 Given an array of size n, sort the array using Merge Sort.

Examples
Input : N=7,arr[]={3,2,8,5,1,4,23}
Output : {1,2,3,4,5,8,23}
Explanation : Given array is sorted in non-decreasing order.
Input : N=5, arr[]={4,2,1,6,7}
Output : {1,2,4,6,7}
Explanation : Given array is sorted in non-decreasing order.
"""

import math


def merge(arr: list, low: int, mid: int, high: int):
    temp = []
    left, right = low, mid + 1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[right])
            right += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[right])
        right += 1
    for i in range(low, high):
        arr[i] = temp[i - low]


def merge_sort(nums: list[int], low: int, high: int):
    mid = math.floor((low + high) / 2)

    merge_sort(nums=nums, low=low, high=mid)

    merge_sort(nums, mid + 1, high)

    merge(nums, low, mid, high)


if __name__ == "__main__":
    sorted = merge_sort([3, 2, 8, 5, 1, 4, 23], low=0, high=7)
    print(sorted)
