"""Problem Statement: Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input:
 nums = [2, 3, 5, -2, 7, -4]
Output:
 15
Explanation:
 The subarray from index 0 to index 4 has the largest sum = 15, which is the maximum sum of any contiguous subarray.

Example 2:
Input:
 nums = [-2, -3, -7, -2, -10, -4]
Output:
 -2
Explanation:
 The largest sum is -2, which comes from taking the element at index 0 or index 3 as the subarray. Since all numbers are negative, the subarray with the least negative number gives the largest sum.
"""


def max_sub_arr(arr: list[int]) -> int:
    """Kadane's algorithm for maximum subarray sum.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    current_sum = max_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    result = max_sub_arr([2, 3, 5, -2, 7, -4])
    print(result)
