"""
Docstring for sliding_window.maximum_average_subarray_i

643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000

"""


def maximum_average_subarray_i(nums: list[int], k: int):
    sum_window = sum(nums[:k])

    max_avg = sum_window / k
    for i in range(k, len(nums)):
        sum_window += nums[i] - nums[i - k]
        curr_wind_avg = sum_window / k
        max_avg = max(max_avg, curr_wind_avg)

    return max_avg


if __name__ == "__main__":
    max_res = maximum_average_subarray_i(nums=[1, 12, -5, -6, 50, 3], k=4)
    print(max_res)
