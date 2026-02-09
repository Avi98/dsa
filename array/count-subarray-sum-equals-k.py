"""
Problem Statement: Given an array of integers and an integer k, return the total number of subarrays whose sum equals k. A subarray is a contiguous non-empty sequence of elements within an array.

Examples
Input : N = 4, array[] = {3, 1, 2, 4}, k = 6
Output: 2
Explanation: The subarrays that sum up to 6 are [3, 1, 2] and [2, 4].

Input: N = 3, array[] = {1,2,3}, k = 3
Output: 2
Explanation: The subarrays that sum up to 3 are [1, 2], and [3].
"""


def count_subarray_sum(lenth: int, arr: list[int], total: int):
    sum_arr = []
    for i in range(len(arr)):
        j = i if i < len(arr) else len(arr) - 1

        if arr[i] + arr[j] == total:
            sum_arr.append((arr[i], arr[j]))
    return sum_arr


if __name__ == "__main__":
    count = count_subarray_sum(lenth=4, arr=[3, 1, 2, 4], total=6)
    print(count)
